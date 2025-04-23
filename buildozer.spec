[app]
title = VS Creator
package.name = vscreator
package.domain = org.creator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3,wav
version = 1.0
requirements = python3,kivy,audioread,pydub,ffmpeg,librosa,numpy
orientation = portrait
osx.python_version = 3
fullscreen = 1
android.api = 31
android.minapi = 21
android.sdk = 24
android.ndk = 23b
android.ndk_api = 21
android.private_storage = True
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.archs = armeabi-v7a,arm64-v8a
android.allow_backup = False
android.build_tools_version = 31.0.0
android.gradle_dependencies = com.android.support:appcompat-v7:28.0.0
android.logcat_filters = *:S python:D

# Ícone (opcional)
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
require_android_sdk = True
