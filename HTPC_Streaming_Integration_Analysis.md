# HTPC Streaming Service Integration Analysis
**Date**: January 2025  
**Goal**: Eliminate AVM70, achieve unified streaming experience through HTPC + D90 with binaural processing

## 🎯 **PROJECT DECISION TREE**

### Core Question: Can External Streamers → HTPC Maintain Binaural Processing?
- **If YES**: Use external streamers for all services (guaranteed 4K HDR + Atmos)
- **If NO**: Use hybrid approach (mix of native HTPC apps + external where needed)

---

## 📊 **PATH ANALYSIS**

### Path A: External Streamers → HTPC Input (Preferred if binaural works)
**Setup**: Roku/Apple TV → HDMI Capture/Audio Input → HTPC → Binaural Processing → D90

#### Audio Routing Options:
1. **HDMI Audio Extraction**
   - External streamer → HDMI audio extractor → USB/Optical to HTPC
   - HTPC processes audio through VoiceMeeter → FlexASIO → Binaural → D90
   - Video: Direct HDMI to display OR captured to HTPC

2. **Digital Audio Input**
   - External streamer → Optical/Coax → HTPC audio interface
   - Maintains Atmos bitstream for processing
   - Video: Separate HDMI to display

#### ✅ **Advantages**:
- All services get native 4K HDR + Atmos from certified devices
- HTPC handles ALL audio processing (binaural, HRTF, room correction)
- Unified audio pipeline regardless of source
- Keep proven streaming device reliability

#### ❓ **Key Unknowns**:
- Can VoiceMeeter → FlexASIO → Binaural chain process external digital audio inputs?
- Does HDMI audio extraction preserve Atmos metadata for processing?
- Latency between audio processing and video display?

---

### Path B: All-in-One HTPC (Backup if Path A fails)
**Setup**: HTPC native apps → VoiceMeeter → FlexASIO → Binaural → D90

#### Service-by-Service Capabilities:

| Service | Windows App/Method | 4K HDR | Atmos | Reliability |
|---------|-------------------|--------|-------|-------------|
| Netflix | Windows Store App | ✅ Yes | ✅ Yes | High |
| Apple TV+ | Windows App/Edge | ✅ Yes | ✅ Yes | High |
| Disney+ | Edge PWA | ⚠️ Mixed | ⚠️ Mixed | Medium |
| Prime Video | Edge | ⚠️ Mixed | ⚠️ Mixed | Medium |
| Max (HBO) | Edge | ⚠️ Mixed | ⚠️ Mixed | Low |
| Paramount+ | Edge | ❌ Rare | ❌ Rare | Low |
| Peacock | Edge | ❌ Rare | ❌ Rare | Low |
| YouTube | Edge/Chrome | ✅ Yes | ❌ No | High |

#### ✅ **Advantages**:
- Single device simplicity
- Guaranteed binaural processing for all content
- No additional hardware needed
- Unified remote control experience

#### ❌ **Disadvantages**:
- Many services limited to 1080p/Stereo on Windows
- Requires per-service testing and optimization
- May need workarounds for DRM restrictions

---

### Path C: Hybrid Approach (Fallback)
**Setup**: Mix of native HTPC apps + external streamers based on service quality

#### Implementation Strategy:
- **HTPC Direct**: Netflix, Apple TV+ (good Windows support)
- **External → HTPC**: Disney+, Prime, Max, Paramount+, Peacock (poor Windows support)
- **Unified Control**: Single remote/interface switches between sources
- **Consistent Audio**: All sources route through HTPC binaural pipeline

---

## 🔬 **TECHNICAL RESEARCH PRIORITIES**

### Priority 1: External Audio Input Testing
**Goal**: Verify if external streamer audio can flow through binaural pipeline

#### Test Setup Required:
1. **HDMI Audio Extractor**
   - Device: ViewHD 4K HDMI Audio Extractor (HDCP 2.2 compatible)
   - Route: Roku → Extractor → USB Audio Interface → HTPC
   
2. **Audio Interface Options**:
   - **Option A**: Focusrite Scarlett Solo (USB, Optical input)
   - **Option B**: Creative Sound Blaster X4 (USB, Optical input)
   - **Option C**: Existing HTPC motherboard optical input (if available)

3. **Software Chain Test**:
   ```
   External Audio Input → VoiceMeeter Virtual Input → FlexASIO → Binaural Processor → D90
   ```

#### Success Criteria:
- [ ] Atmos content from Roku maintains object metadata through audio extraction
- [ ] VoiceMeeter can route external audio inputs to ASIO output
- [ ] Binaural processor (HeSuVi/Virtuoso) can process external Atmos streams
- [ ] Audio/video sync maintained (acceptable latency)
- [ ] All streaming services deliver expected audio quality

---

### Priority 2: Native HTPC App Evaluation
**Goal**: Document actual 4K HDR + Atmos capability per service on target HTPC hardware

#### Test Protocol:
1. **Hardware Verification**:
   - Confirm GPU supports 4K HDR output
   - Enable Windows HDR mode
   - Set audio output to "Dolby Atmos for Headphones"

2. **Per-Service Testing**:
   - Test known 4K HDR titles per service
   - Test known Atmos titles per service
   - Document actual resolution/audio format delivered
   - Note any service-specific limitations

3. **Integration Testing**:
   - Verify each service works with unified launcher (Playnite)
   - Test remote control navigation
   - Confirm audio routing through binaural pipeline

---

## 💰 **COST ANALYSIS**

### Path A: External → HTPC Input
**Required Hardware**:
- HDMI Audio Extractor: $50-100
- USB Audio Interface: $100-200 (if motherboard lacks optical input)
- **Total**: $150-300

### Path B: All-in-One HTPC
**Required Software**:
- Playnite: FREE
- Service apps: FREE
- **Total**: $0

### Path C: Hybrid
**Hardware**: Same as Path A for external services
**Total**: $150-300

---

## 📋 **IMPLEMENTATION ROADMAP**

### Phase 1: Research & Testing (Current Priority)
1. **External Input Feasibility**
   - Research HDMI audio extractors with Atmos passthrough
   - Test VoiceMeeter external input routing capabilities
   - Verify binaural processor external input support

2. **Native App Baseline**
   - Install and test Netflix Windows app (known working case)
   - Document current HTPC 4K HDR + Atmos output capability
   - Test Playnite integration and remote control

### Phase 2: Proof of Concept
1. **If External Input Viable**:
   - Purchase HDMI audio extractor + interface
   - Set up Roku → HTPC audio routing
   - Test full pipeline: Roku Atmos → Binaural → D90

2. **If External Input Not Viable**:
   - Focus on native HTPC app optimization
   - Set up unified launcher with working services
   - Document service limitations and workarounds

### Phase 3: Full Implementation
- Deploy chosen solution
- Optimize remote control experience  
- Document final configuration
- Create user guide for daily operation

---

## 🤔 **DECISION FACTORS**

### Choose Path A (External → HTPC) if:
- External audio input preserves Atmos processing capability
- Video sync issues are manageable
- 4K HDR + Atmos from all services is priority

### Choose Path B (All-in-One HTPC) if:
- External input doesn't support binaural processing
- Simplicity is more important than universal 4K HDR
- Willing to accept service quality limitations

### Choose Path C (Hybrid) if:
- External input works but has limitations
- Want to optimize per-service quality
- Comfortable with more complex setup

---

## 🎯 **IMMEDIATE NEXT STEPS**

1. **Research Phase** (This Week):
   - [ ] Find HDMI audio extractors that preserve Atmos metadata
   - [ ] Test VoiceMeeter external input capabilities
   - [ ] Verify Virtuoso/HeSuVi external input support

2. **Baseline Testing** (Next Week):
   - [ ] Install Netflix Windows app on HTPC
   - [ ] Test 4K HDR + Atmos → D90 pipeline
   - [ ] Install Playnite and configure basic launcher

3. **Decision Point** (Week 3):
   - [ ] Choose implementation path based on test results
   - [ ] Order required hardware if external input route chosen
   - [ ] Begin full implementation of selected approach

---

*This document will be updated as research and testing progresses.*
