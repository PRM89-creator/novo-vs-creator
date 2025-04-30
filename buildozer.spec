[app]
title = VS Creator
package.name = vscreator
package.domain = org.vscreator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3,wav
version = 1.0
requirements = python3,kivy==2.3.0,android  # Kivy fixo na 2.3.0 + android
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.minapi = 21
android.sdk = 33  # SDK atualizado (34 pode causar conflitos)
android.ndk = 25b  # NDK compatível com Kivy
android.ndk_api = 21
android.private_storage = True
android.arch = armeabi-v7a,arm64-v8a  # Arquiteturas padrão
p4a.branch = master  # Adicionado para garantir compatibilidade

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = .buildozer
bin_dir = bin
android.accept_sdk_license = True  # Essencial para CI/CD
