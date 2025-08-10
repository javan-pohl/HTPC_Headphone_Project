# DAC Analysis and Comparison Report
**Date**: January 2025  
**Objective**: Analyze current DAC performance vs. potential upgrades and understand audio quality differences

---

## 🎯 **PROJECT GOALS & QUESTIONS**

### **Primary Questions**
1. **Anthem AVM70 DAC Quality**: What DAC chips does the AVM70 use and how do they perform?
2. **SMSL SU-1 Advantage**: Why does the SU-1 seem to have a substantial advantage over the AVM70?
3. **AVR Noise Issues**: Do AVR/pre-processors add substantial noise due to video hardware integration?
4. **SU-1 EQ Question**: Does the SU-1 have any default audio EQ curve affecting bass response?
5. **Upgrade Path**: How do higher-end DACs like the Topping D90 III Sabre compare to current options?

---

## 📊 **CURRENT DAC INVENTORY**

### **Anthem AVM70**
- **DAC Chips**: ESS ES9038Q2M (main channels), ES9010K2M (Zone 2/Subwoofer outputs)
- **Background**: Originally used AKM AK4490 chips, switched to ESS after AKM factory fire
- **Channel Configuration**: 8 pieces of ES9038Q2M for main 15 channels + 2 pieces ES9010K2M for secondary outputs
- **Performance**: ~110dB SNR, 10.7V maximum output, good specs for an AVR/pre-pro
- **Implementation**: Dual DAC chips used - ES9038Q2M for main, ES9010K2M for Zone 2/subwoofers

### **SMSL SU-1**
- **DAC Chip**: AKM AK4493SEQ (32-bit stereo)
- **Price**: $80 USD
- **Features**: USB-C (power & data), Optical, Coaxial inputs, RCA outputs
- **Performance**: 121dB dynamic range, 121dB SNR, THD+N: 0.00013% (-117dB)
- **Power**: <5W consumption, USB powered
- **Size**: 96×27×78mm, 195g - very compact desktop unit

---

## 🔍 **KEY FINDINGS**

### **1. Anthem AVM70 DAC Analysis**
- **✅ Good Quality**: Uses flagship ESS ES9038Q2M chips (not budget chips)
- **✅ Proper Implementation**: Multiple DAC chips for different channels shows thoughtful design
- **⚠️ Complexity**: Integration with video processing and multichannel processing may introduce noise
- **💡 Discovery**: The switch from AKM to ESS was due to supply chain issues, not quality reasons

### **2. AVR/Pre-Processor Noise Investigation**
**Research Results**:
- **📈 Measurable Differences**: Studies show AVRs do add ~1dB more noise when processing multichannel vs 2-channel
- **🔌 HDMI Integration**: Video processing can introduce electrical noise into analog pathways
- **⚡ Power Supply**: Shared power supplies between video and audio sections can cause interference
- **🎯 Key Quote**: "To achieve almost 110dB in the audible spectrum is quite something especially considering the complexity of an AV receiver with all the potential electrical noise sources inside the box"
- **✅ Still Excellent**: Modern AVRs like AVM70 achieve impressive ~110dB SNR despite complexity

### **3. Practical Signal Chain Analysis**
**Your Current Audio Chains**:
- **Chain A**: HTPC → SMSL SU-1 → Topping L50 → Hype 4 (balanced cable)
- **Chain B**: HTPC → Anthem AVM70 → Topping L50 → Hype 4

**Why SU-1 Chain Measures Better - Technical Deep Dive**:
1. **Longer, busier signal path in AVM70**: Source selection, muting relays, buffers, protection circuits, and volume control stages add op-amps and resistive networks that raise noise and distortion
2. **Shared, noisy environment**: Large digital subsystems (HDMI, video processors, network/Wi-Fi, MCU) and their clocks/ground currents couple into analog section more easily than in compact DAC with tight layout
3. **Power-supply architecture**: Multiple rails and larger switch-mode supplies in AVPs raise analog noise floor; modern DACs use extremely quiet, point-of-load regulation tailored to analog output stage
4. **Interface-dependent performance**: AVM70 shows **worse dynamic range via HDMI than via coax/USB** due to clocking/isolation differences - HDMI path isn't as clean as 2-ch USB/coax DAC

**Concrete Performance Numbers**:
- **SMSL SU-1**: ~116-120 dB SINAD (transparent performance)
- **Topping D90 III Sabre**: ~124 dB SINAD (chart-topper territory)  
- **Anthem AVM70**: ~102-106 dB SINAD (typical for high-end AV processors)
- **SMSL SU-10** (flagship reference): ~132 dB balanced dynamic range

### **4. SMSL SU-1 Analysis**
**Why It Sounds Better**:
- **🎯 Purpose-Built**: Dedicated audio-only design with no video interference
- **🔋 Clean Power**: Simple USB power with minimal switching noise
- **📦 Isolation**: Smaller form factor with better component isolation
- **⚡ No Compromises**: No multichannel processing, room correction, or video circuits to introduce noise

**Sound Characteristics**:
- **🎵 Balanced Tonality**: Well-balanced frequency response, not overly warm or bright
- **🎯 Transparent**: Clean, uncolored signal - flat 20Hz-10kHz, slight treble dip
- **❌ No EQ**: Does NOT have default EQ curves - any bass differences likely due to cleaner presentation
- **💪 Dynamics**: Excellent dynamic range and detail retrieval for the price

### **5. Bass Response Question - SOLVED**
**Your AVM70 bass issues are likely NOT due to SU-1 having different EQ**:
- ✅ SU-1 has no default EQ curves
- ❌ Check AVM70 settings - it may have:
  - Old room correction settings still active
  - Bass management incorrectly configured
  - Subwoofer routing issues
  - Speaker size settings incorrect

---

## 🔌 **BALANCED CONNECTION ANALYSIS**

### **Benefits of Balanced DAC → L50 Chain**
**Going XLR from DAC → L50 TRS inputs provides**:
1. **Common-mode noise rejection & ground-loop immunity** over longer runs or with noisy PCs (primary benefit)
2. **+6 dB nominal output level** (4 Vrms vs ~2 Vrms RCA) raises signal relative to L50's input-referred noise
3. **Lower L50 gain operation** - run Low gain for hiss-sensitive IEMs like Hype 4
4. **Marginally better crosstalk** in true differential chains

### **Topping L50 Balanced Configuration**
- **Inputs**: Balanced line via dual 6.35mm TRS (one TRS per channel) - NOT XLR sockets
- **Required Cables**: XLR-to-dual-TRS interconnects from DAC
- **Headphone Outputs**: 4-pin XLR and 6.35mm jacks have essentially same power/specs
- **Noise Floor**: Extremely low, suitable for sensitive IEMs on Low gain
- **Gain Settings**: Use Low gain with balanced input for black backgrounds

### **Cable Recommendation for Your Setup**
**HTPC → DAC (USB) → L50 (TRS-balanced) → Hype 4**:
- **DAC Output**: XLR balanced (4 Vrms)
- **Cable Type**: XLR male to dual 6.35mm TRS
- **L50 Setting**: Low gain, balanced TRS inputs
- **DAC Setting**: ~3-4 Vrms output (0 dBFS fixed) for digital attenuation headroom

---

## 📈 **PERFORMANCE COMPARISONS**

### **Current Setup Performance**
| Metric | Anthem AVM70 | SMSL SU-1 | Advantage |
|--------|--------------|-----------|-----------|
| **SINAD** | ~102-106dB | ~116-120dB | SU-1 (+14dB) |
| **Dynamic Range** | ~110dB | 121dB | SU-1 (+11dB) |
| **THD+N** | Not specified | 0.00013% (-117dB) | SU-1 |
| **Interface Quality** | HDMI < Coax/USB | USB optimized | SU-1 |
| **Noise Sources** | Video, multichannel, room correction | Audio only | SU-1 |
| **Implementation** | Complex, many subsystems | Simple, dedicated | SU-1 |

### **Why SU-1 Outperforms AVM70**
1. **Dedicated Design**: Audio-only vs. complex AV processor
2. **Cleaner Power**: USB vs. complex internal power supply
3. **Less Interference**: No video processing, HDMI switching, room correction
4. **Simpler Signal Path**: Minimal processing between input and output
5. **Newer Implementation**: Purpose-built for audio quality

---

## 🚀 **UPGRADE OPTIONS ANALYSIS**

### **Topping D90 III Sabre ($899)**
**Specifications**:
- **DAC Chips**: Dual ES9039SPRO (latest flagship ESS chips)
- **Performance**: ~124dB SINAD (chart-topper territory)
- **Features**: USB, I²S, Optical, Coaxial, AES, Bluetooth 5.1
- **Outputs**: Both RCA (2.1V/2.6V) and XLR (4.2V/5.2V) with selectable levels
- **MQA**: Full hardware decoding support

**Sound Character**:
- **🎯 Neutral & Transparent**: Very linear frequency response  
- **⚡ Fast & Dynamic**: Excellent transient response and dynamics
- **🔍 Highly Revealing**: Exceptional detail retrieval without harshness
- **📊 Technical**: More analytical than musical, excellent for critical listening

### **SMSL SU-10 ($999)**
**Specifications**:
- **DAC Chips**: Flagship ESS implementation
- **Performance**: ~132dB balanced dynamic range (state-of-the-art)
- **Features**: Maximum dynamic range/headroom, filters, "sound color" modes, Bluetooth, preamp features
- **Outputs**: Full-size balanced XLR outputs
- **Build**: Premium construction with advanced drivers

**Advantages**:
- **🏆 Maximum Dynamic Range**: Industry-leading measurements
- **🎛️ Feature Rich**: Advanced controls and connectivity options  
- **🔌 Connectivity**: More inputs and output options
- **⚡ Headroom**: Excellent for digital attenuation without SNR loss

### **Three-Way Comparison**
| Aspect | SMSL SU-1 ($80) | Topping D90 III Sabre ($899) | SMSL SU-10 ($999) |
|--------|------------------|-------------------------------|-------------------|
| **SINAD** | ~116-120dB | ~124dB | Not specified |
| **Dynamic Range** | 121dB | Excellent | ~132dB |
| **Value** | Exceptional | Good | Good |
| **Build Quality** | Good aluminum | Premium | Premium |
| **Features** | Basic but complete | Extensive | Maximum |
| **Price/Performance** | Outstanding | Good | Good |

---

## 🎵 **SOUND CHARACTER PROFILES**

### **Anthem AVM70**
- **Signature**: Warm, smooth, forgiving
- **Strengths**: Musical, room correction, multichannel processing
- **Weaknesses**: Added complexity, potential noise from video integration
- **Best For**: Home theater, multichannel music, convenience

### **SMSL SU-1**  
- **Signature**: Neutral, clean, transparent
- **Strengths**: Incredible value, simple operation, clean power
- **Weaknesses**: Basic features, no volume control, small size
- **Best For**: Budget audiophiles, desktop setups, dedicated 2-channel

### **Topping D90 III Sabre**
- **Signature**: Analytical, transparent, reference
- **Strengths**: Exceptional measurements, features, build quality
- **Weaknesses**: Can be too revealing for poor recordings, analytical
- **Best For**: Critical listening, reference systems, detail retrieval

---

## 💡 **RECOMMENDATIONS**

### **Immediate Actions - AVM70 Bass Issues**
1. **🔧 Check Bass Management**: Verify speaker sizes and crossover settings
2. **🎛️ Disable Room Correction**: Temporarily turn off ARC to test
3. **🔊 Verify Subwoofer Settings**: Check routing and level settings  
4. **⚖️ A/B Test**: Direct comparison between AVM70 and SU-1 with identical settings

### **Practical System Configuration**

#### **Dual-Path Setup (✅ Recommended)**
1. **Keep AVM70** for theater: HTPC → AVM70 (HDMI) for multichannel Atmos
2. **Dedicated headphone chain**: HTPC USB → standalone DAC → L50 (balanced TRS) → Hype 4
3. **Bypass AVM70** for critical listening to avoid HDMI/AVP noise and shorten signal path
4. **Cable Setup**: XLR-to-dual-TRS from DAC to L50, L50 on Low gain, DAC at ~3-4 Vrms output

#### **DAC Selection Priority**
1. **Budget Option (✅ Current)**: Keep SMSL SU-1 - exceptional value, already transparent performance
2. **Maximum Dynamic Range**: SMSL SU-10 ($999) - 132dB DR, full features, preamp mode
3. **Top Linearity/SINAD**: Topping D90 III Sabre ($899) - 124dB SINAD, excellent drivers
4. **Choose by features/price** - both D90 III and SU-10 are audibly transparent

#### **System Optimization**
- **L50 Settings**: Low gain with balanced input for black backgrounds with sensitive IEMs
- **Digital Volume**: Use HTPC app attenuation (plenty of headroom with high-DR DACs)
- **Cable Quality**: XLR-to-dual-TRS interconnects for balanced operation
- **Interface**: USB from HTPC avoids HDMI-related noise issues

---

## 🔬 **TECHNICAL NOTES**

### **AVR vs Dedicated DAC Reality**
- **Myth**: "AVRs always have terrible DACs"
- **Reality**: Modern AVRs like AVM70 use excellent DAC chips
- **Truth**: The limitation is implementation complexity, not chip quality
- **Evidence**: AVM70's ES9038Q2M is the same chip used in many high-end dedicated DACs

### **Measurements vs. Listening**
- **SMSL SU-1**: Measures very well for $80, punches far above its weight
- **Topping D90 III**: Measures exceptionally, among the best available
- **AVM70**: Measures well considering complexity, ~110dB SNR is respectable
- **Real-World**: Differences become smaller in actual listening vs measurements

---

## 📋 **CONCLUSION**

### **Why SU-1 Outperforms AVM70**
✅ **Dedicated audio design** vs. complex AV processor  
✅ **Cleaner power supply** and simpler signal path  
✅ **No video interference** or multichannel processing noise  
✅ **Modern implementation** optimized for audio quality  

### **Bass Issue Resolution**
❌ **NOT due to SU-1 EQ** - it has flat response  
✅ **Check AVM70 settings** - likely configuration issue  
✅ **Room correction** may be affecting bass response  

### **Upgrade Recommendation**
🎯 **SMSL SU-1 is the sweet spot** - exceptional performance for $80  
💰 **Topping D90 III** offers modest improvements for 11x the cost  
🏆 **Best value** is keeping the SU-1 and fixing AVM70 bass issues  

**Bottom Line**: The SU-1's advantage comes from dedicated design and implementation excellence, not magic. For $80, it delivers performance that challenges units costing 10x more.

---

## 📚 **SOURCES & REFERENCES**
- Anthem AVM70 technical specifications and forum discussions
- SMSL SU-1 professional reviews (TechPowerUp, iiWi Reviews, SoundNews)
- Topping D90 III Sabre reviews (Headfonics, ASR measurements)
- AVR noise analysis (Archimago's measurements, Audioholics forums)
- Technical discussions from Audio Science Review and AVS Forum

*Last Updated: January 2025*
