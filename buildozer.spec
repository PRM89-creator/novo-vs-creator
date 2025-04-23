[app]
title = VS Creator
package.name = vscreator
package.domain = org.vscreator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3,wav
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
android.private_storage = True
android.arch = armeabi-v7a,arm64-v8a
# Se usar arquivos de áudio ou manipulação, adicione aqui:
# requirements = python3,kivy,pydub,ffmpeg

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = .buildozer
bin_dir = bin
# Comente a linha abaixo se for rodar localmente em outro ambiente
# Se estiver usando GitHub Actions, mantenha assim:
android.accept_sdk_license = True
