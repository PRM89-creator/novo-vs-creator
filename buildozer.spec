[app]
title = VS Creator
package.name = vscreator
package.domain = org.vscreator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3,wav
version = 1.0
requirements = python3==3.9.13,kivy==2.3.0,android
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.minapi = 21
android.sdk_version = 33  # Usar sdk_version em vez de sdk
android.ndk_version = 25b  # Usar ndk_version em vez de ndk
android.ndk_api = 21
android.private_storage = True
android.archs = armeabi-v7a,arm64-v8a  # Usar archs (plural) em vez de arch
p4a.branch = develop  # Branch mais estável que master

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = .buildozer
bin_dir = bin
android.accept_sdk_license = True

# Configurações recomendadas para CI
android.skip_update = True  # Evita verificações desnecessárias
android.verbose = True  # Mais detalhes nos logs
