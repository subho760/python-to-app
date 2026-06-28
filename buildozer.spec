[app]

# (str) Title of your application
title = Dragon Hole

# (str) Package name
package.name = dragonhole

# (str) Package domain (needed for android packaging)
package.domain = org.subho

# (list) Source files to include (including the patterns)
source.include_exts = py,png,jpg,jpeg,spec

# (list) List of directories to include
source.include_dirs = images

# (str) Icon of the application
icon.filename = logo.png

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip apply patch to platform
android.accept_sdk_license = True

# (str) The Android arch to target (both standard 32 and 64 bit architectures)
android.archs = arm64-v8a, armeabi-v7a
