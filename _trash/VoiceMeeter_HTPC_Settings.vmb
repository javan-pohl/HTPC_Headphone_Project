# VoiceMeeter Banana Settings for HTPC 5.1.2 Setup
# Load this via: Menu -> Load Settings in VoiceMeeter Banana
# 
# CRITICAL SETTINGS FOR 8-CHANNEL SUPPORT:
# - Patch Insert enabled (creates 32-channel ASIO device)
# - VAIO configured for multichannel input from Kodi
# - A1 output for monitoring

[VBVMR]
# Core VoiceMeeter Settings
version=3.0.2.8
BusMode=2

# CRITICAL: Enable Patch Insert for FlexASIO bridge
PatchInsert=1

# Input Strips Configuration
Strip[0].name=VAIO-Kodi
Strip[0].mute=0
Strip[0].solo=0
Strip[0].gain=0.0
Strip[0].gate=0.0
Strip[0].comp=0.0
Strip[0].A1=1
Strip[0].A2=0
Strip[0].A3=0
Strip[0].B1=0
Strip[0].B2=0

Strip[1].name=HW Input 1
Strip[1].mute=1
Strip[1].solo=0
Strip[1].gain=0.0
Strip[1].A1=0
Strip[1].A2=0
Strip[1].A3=0
Strip[1].B1=0
Strip[1].B2=0

Strip[2].name=HW Input 2
Strip[2].mute=1
Strip[2].solo=0
Strip[2].gain=0.0
Strip[2].A1=0
Strip[2].A2=0
Strip[2].A3=0
Strip[2].B1=0
Strip[2].B2=0

Strip[3].name=AUX Virtual
Strip[3].mute=1
Strip[3].solo=0
Strip[3].gain=0.0
Strip[3].A1=0
Strip[3].A2=0
Strip[3].A3=0
Strip[3].B1=0
Strip[3].B2=0

Strip[4].name=VAIO3 Virtual
Strip[4].mute=1
Strip[4].solo=0
Strip[4].gain=0.0
Strip[4].A1=0
Strip[4].A2=0
Strip[4].A3=0
Strip[4].B1=0
Strip[4].B2=0

# Output Bus Configuration
Bus[0].name=A1-Monitors
Bus[0].mute=0
Bus[0].gain=0.0
Bus[0].return=0.0
Bus[0].monitor=0

Bus[1].name=A2-Unused
Bus[1].mute=1
Bus[1].gain=0.0
Bus[1].return=0.0
Bus[1].monitor=0

Bus[2].name=A3-Unused
Bus[2].mute=1
Bus[2].gain=0.0
Bus[2].return=0.0
Bus[2].monitor=0

Bus[3].name=B1-Virtual
Bus[3].mute=1
Bus[3].gain=0.0
Bus[3].return=0.0
Bus[3].monitor=0

Bus[4].name=B2-Virtual
Bus[4].mute=1
Bus[4].gain=0.0
Bus[4].return=0.0
Bus[4].monitor=0

# System Settings
Option.SampleRate=48000
Option.BufferSize=512
Option.ASIOBufferSize=512
Option.SRConversion=1
Option.PreferredMainSR=48000
Option.WDMInputExclusiveMode=1
Option.WDMOutputExclusiveMode=0

# Engine Settings
Option.Engine.MultiCoreMME=1
Option.Engine.MultiCoreWDM=1
Option.Engine.MultiCoreKS=1
Option.Engine.MultiCoreDX=1

# Advanced Settings for Stability
Option.Delay.VAIO=1024
Option.Delay.AUX=1024
Option.Delay.VAIO3=1024

# Color Themes (Optional)
Option.Color=0