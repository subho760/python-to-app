[app]

# (str) Title of your application
title = Dragon Hole

# (str) Package name
package.name = dragonhole

# (str) Package domain (needed for android packaging)
package.domain = org.nightshadow

# (str) Source code directory where main.py resides
source.dir = .

# (list) Source files to include (crucial for loading your web stack)
source.include_exts = py,png,jpg,kv,atlas,html,css,js

# (list) Source directories to include
source.include_dirs = www

# (str) Application versioning (String representation)
version = 1.0.0

# (int) Android version code (Increments with every Play Store update)
android.numeric_version = 1

# (str) Icon of the application (Must be a PNG file in your root folder)
icon.filename = icon.png

# (list) Application requirements
requirements = python3,kivy,android

# (list) Supported orientations
orientation = portrait

# ----------------------------------
# Android specific configuration
# ----------------------------------

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions requested by app (Internet needed for internal webview hosting)
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use (Leave blank so the Action matches it flawlessly)
android.ndk = 

# (bool) Enable AndroidX architecture
android.enable_androidx = True

# (list) Architectures to build for (Covers 99% of modern devices)
android.archs = arm64-v8a, armeabi-v7a

# (str) Default build target format (The YAML pipeline will auto-toggle this anyway)
android.target = aab


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
