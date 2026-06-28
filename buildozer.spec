[app]

# (str) Title of your application
title = Dragon Hole

# (str) Package name
package.name = dragonhole

# (str) Package domain (needed for android packaging)
package.domain = org.subho

# (str) Source code directory where main.py lives (DO NOT REMOVE)
source.dir = .

# (list) Source files to include (including the patterns)
source.include_exts = py,png,jpg,jpeg,spec

# (list) List of directories to include
source.include_dirs = images

# (str) Application versioning configuration (DO NOT REMOVE)
version = 1.0.0

# (str) Icon of the application
icon.filename = logo.png

# (list) Application requirements
requirements = python3,kivy

# (int) Target Android API (Bumped to 34 to satisfy Play Protect warnings)
android.api = 34

# (int) Minimum API your APK will support
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip apply patch to platform
android.accept_sdk_license = True

# (str) The Android architectures to target
android.archs = arm64-v8a, armeabi-v7a

# (str) Supported orientations
orientation = portrait

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug and stdout)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
