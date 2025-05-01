[app]
title = VS Creator
package.name = vscreator
package.domain = org.vscreator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3,wav,ogg
version = 1.0
requirements = 
    python3==3.9.13,
    kivy==2.3.0,
    librosa==0.10.1,
    numpy==1.26.4,
    pydub==0.25.1,
    android,
    ffmpeg-python==0.2.0

orientation = portrait
fullscreen = 1

android.permissions = 
    INTERNET,
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE,
    RECORD_AUDIO

android.minapi = 21
android.sdk_version = 33
android.ndk_version = 25b
android.ndk_api = 21
android.archs = armeabi-v7a,arm64-v8a
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = .buildozer
bin_dir = bin
android.accept_sdk_license = True
android.skip_update = True
