[app]

# (str) Title of your application
title = VS Creator

# (str) Package name
package.name = vscreator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.creator

# (str) Source code where the main.py is located
source.dir = .

# (str) Application versioning
version = 1.0.0

# (str) Application entry point
entrypoint = main.py

# (list) Permissions
android.permissions = INTERNET

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Supported platforms
android.archs = armeabi-v7a, arm64-v8a

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png


[buildozer]

# (str) Target platform
target = android

# (str) Log level (0 = error only, 1 = warning, 2 = info, 3 = debug, 4 = trace)
log_level = 2

# (bool) Display warning if buildozer is run as root (default: 1)
warn_on_root = 1

# (str) Android SDK version to use
# CORRIGIDO PARA EVITAR ERRO DE AIDL
android.api = 30

# (str) Android build tools version
# CORRIGIDO PARA USAR UMA VERSÃO QUE TEM O AIDL PRESENTE
android.build_tools_version = 30.0.3

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android entry point, default is ok
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, supported themes are:
#       'light', 'dark', or custom.
# android.theme = '@android:style/Theme.NoTitleBar'
