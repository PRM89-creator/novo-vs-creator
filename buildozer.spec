[app]

# Nome do app
title = VS Creator

# Nome do pacote
package.name = vscreator

# Domínio reverso
package.domain = org.creator

# Código-fonte
source.dir = .

# Versão do app
version = 1.0.0

# Arquivo principal
entrypoint = main.py

# Permissões Android
android.permissions = INTERNET

# Orientação da tela
orientation = portrait

# Tela cheia
fullscreen = 1

# Arquiteturas suportadas
android.archs = armeabi-v7a, arm64-v8a

# Ícone do app
icon.filename = %(source.dir)s/icon.png

# Requisitos de dependências
requirements = python3,kivy

# Tela de carregamento
presplash.filename = %(source.dir)s/presplash.png

# Filtros de log do logcat
logcat_filters = *:S python:D

# Copiar libs (necessário para algumas builds)
android.copy_libs = 1


[buildozer]

# Plataforma de destino
target = android

# Nível de log
log_level = 2

# Aviso se rodar como root
warn_on_root = 1

# API do Android (SDK)
android.api = 30

# Build Tools com suporte ao AIDL
android.build_tools_version = 30.0.3

# NDK compatível com o Buildozer
android.ndk = 25b

# Atividade de entrada (padrão do Kivy)
android.entrypoint = org.kivy.android.PythonActivity

# Tema da interface
android.theme = 'light'

# Diretório de cache da Gradle (mantém padrão)
# android.gradle_cache_dir =

# Armazenamento privado (mantém dados internos)
android.private_storage = True
