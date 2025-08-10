# HTPC Audio System Progress Report

## Current System Overview
**Goal**: Replace physical players + Anthem AVM70 with laptop-based high-quality audio system
**Target Quality**: Match or exceed AVM70 reference system performance
**Listening Setup**: Laptop → USB → Topping D90 DAC → Topping L50 Amp → 64 Audio Hype 4 IEMs

## Current Configuration
- **Audio Chain**: Laptop → USB → Topping D90 DAC → Topping L50 Amp (1/4" to XLR cable, Low gain)
- **Software Path**: Kodi → WASAPI Exclusive → Voicemeeter Input (8ch) → Mix Down A → WASAPI D90
- **Windows Settings**: Voicemeeter Input set to Stereo, 192kHz
- **Kodi Settings**: 7.1 output, 192kHz, WASAPI Exclusive to Voicemeeter Input

## Testing Journal

### Session Date: [Current Date]

#### Kodi Configuration Success
- **Kodi 22.0-ALPHA1** configured for optimal audio quality
- **WASAPI Exclusive** output successfully enabled (eliminates Windows audio processing)
- **7.1 channel** configuration working (8 channels confirmed in Voicemeeter)
- **192kHz support** confirmed (critical for favorite reference: Akira 5.1 192kHz Dolby mix)
- **Audio quality**: Power and clarity **matching Anthem AVM70 reference**

#### Technical Discoveries
- **Windows Voicemeeter Input**: Set to Stereo, 192kHz (maximum supported)
- **Multi-channel processing**: 8-channel input properly downmixed via "Mix Down A"
- **Stereo Windows setting**: May be helping eliminate awkward rear surround artifacts
- **Signal path optimization**: Full WASAPI chain eliminates DirectSound processing

#### Audio Quality Assessment
**Positive Results:**
- **Power and clarity matching AVM70**: Significant achievement
- **Clean signal path**: WASAPI Exclusive delivering expected quality
- **Multi-channel preservation**: Full surround information reaching downmix stage
- **High-res support**: 192kHz capability confirmed for reference material

**Ongoing Issues:**
- **Static occurrences**: Persistent electrical noise issue (non-HVAC related)
- **Pause/restart stuttering**: Massive stuttering and static on playback control
- **Buffer-related artifacts**: Suggests audio buffering/driver issues
- **USB cable unknown spec**: Using included D90 cable (specification unknown)

#### Dolby Access Testing
**Spatial Audio Performance:**
- **Object tracking**: Effective sound object movement through soundfield
- **Surround positioning**: Impressive surround sound placement
- **Overhead limitation**: No effective overhead positioning detected (expected limitation with headphones)

**Dynamic Range Impact:**
- **Compression artifacts**: Noticeable dynamic range reduction
- **Power limitation**: Loud elements lack the startling power of direct route
- **Clarity degradation**: Detail and clarity taking measurable hit
- **Volume scaling issues**: Voices seem loud before sound effects reach full impact

**Configuration Notes:**
- **Limited settings available** in Dolby Access
- **Manual EQ configured** with Volume Leveler set to "Off"
- **Trade-off identified**: Spatial enhancement vs. dynamic range/power

#### Hardware Configuration
- **DAC to Amp connection**: 1/4" to XLR patch cable
- **L50 gain setting**: Low gain
- **USB cable**: Unknown specification (D90 included cable)

## Current Status Assessment

### Achievements
1. **Audio quality parity** with AVM70 reference system achieved
2. **Bit-perfect signal path** established via WASAPI Exclusive
3. **Multi-channel processing** working correctly
4. **High-resolution support** confirmed (192kHz)

### Outstanding Issues
1. **Static/electrical noise** requiring hardware solution (USB isolator recommended)
2. **Playback control artifacts** suggesting buffer/driver optimization needed
3. **Dolby processing trade-offs** between spatial enhancement and dynamic range

### Next Priorities
1. **USB isolator implementation** (Topping HS02) for static elimination
2. **Buffer optimization** for playback stability
3. **Alternative spatial audio solutions** that preserve dynamic range
4. **USB cable specification verification** and potential upgrade

## Technical Notes
- **Windows audio format limitation**: Voicemeeter Input maximum 192kHz
- **Kodi passthrough options**: Not found in current configuration
- **Direct route performance**: Current non-Dolby configuration preferred for dynamic range
- **Spatial audio challenge**: Balancing surround enhancement with audio fidelity

---
*Report created: [Current Date]*  
*Last updated: [Current Date]*
