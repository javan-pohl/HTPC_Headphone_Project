use hound::{WavWriter, WavSpec};
use std::env;
use std::fs::File;
use std::io::Read;
use std::path::Path;
use truehd::{TrueHDReader, TRUEHD_SYNC};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = env::args().collect();
    if args.len() != 3 {
        eprintln!("Usage: {} <input_truehd_file> <output_wav_file>", args[0]);
        return Ok(());
    }

    let input_path = Path::new(&args[1]);
    let output_path = Path::new(&args[2]);

    println!("Opening input file: {:?}", input_path);
    let mut file = File::open(input_path)?;
    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer)?;
    println!("Read {} bytes from input file.", buffer.len());

    let mut reader = TrueHDReader::new(&buffer);

    // Find the first sync word to get stream info
    let first_frame = reader
        .find_sync()
        .ok_or("Could not find a TrueHD sync word in the file.")?
        .1;

    let stream_info = first_frame.stream_info().ok_or("Failed to parse stream info")?;
    println!("Stream info found: {:?}", stream_info);

    let spec = WavSpec {
        channels: stream_info.channels as u16,
        sample_rate: stream_info.sample_rate,
        bits_per_sample: 32, // Use 32 bits for WAV to accommodate 24-bit samples
        sample_format: hound::SampleFormat::Int,
    };
    println!("WAV spec created: {:?}", spec);

    let writer = WavWriter::create(output_path, spec)?;
    let mut pcm_writer = writer.get_i32_writer(stream_info.major_sync_header.duration as u32);

    // Reset the reader to the beginning to decode all frames
    reader = TrueHDReader::new(&buffer);
    let mut frame_count = 0;

    println!("Starting decoding process...");
    loop {
        match reader.find_sync() {
            Some((_, frame)) => {
                let pcm_samples = frame.decode_frame()?;
                for &sample in pcm_samples.iter() {
                    pcm_writer.write_sample(sample);
                }
                frame_count += 1;
                if frame_count % 100 == 0 {
                    print!("\rDecoded {} frames...", frame_count);
                }
            }
            None => {
                println!("\nNo more sync words found. Reached end of stream.");
                break;
            }
        }
    }

    println!("\nDecoding complete. Wrote {} frames.", frame_count);
    pcm_writer.flush()?;
    println!("Output file saved to: {:?}", output_path);

    Ok(())
}
