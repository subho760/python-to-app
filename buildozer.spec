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

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# WebView implementation relies on Kivy and android extensions
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

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Enable AndroidX architecture (Required for modern Android WebView execution)
android.enable_androidx = True

# (list) Architectures to build for (Covers 99% of modern devices)
android.archs = arm64-v8a, armeabi-v7a

# (str) Default build target format (The YAML pipeline will auto-toggle this anyway)
android.target = aab

