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

# (list) Application requirements
requirements = python3,kivy

# (str) Presplash of the application
presplash.filename = %(source.dir)s/presplash.png

# (str) Supported orientation
orientation = portrait

# (bool) Android logcat filters to use
logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1


[buildozer]

# (str) Target platform
target = android

# (str) Log level (0 = error only, 1 = warning, 2 = info, 3 = debug, 4 = trace)
log_level = 2

# (bool) Display warning if buildozer is run as root (default: 1)
warn_on_root = 1

# (str) Android SDK version to use
android.api = 30

# (str) Android build tools version
android.build_tools_version = 30.0.3

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android entry point, default is ok
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, supported themes are: 'light', 'dark', or custom.
android.theme = 'light'

# (str) Path to build artifact storage, optional (default: .buildozer)
# build_dir = .buildozer

# (str) Path to the .gradle folder used to store gradle caches (default: ~/.gradle)
# android.gradle_cache_dir =

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True
