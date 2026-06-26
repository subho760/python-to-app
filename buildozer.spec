[app]
title = Dragon Hole
package.name = dragonhole
package.domain = org.nightshadow
source.dir = .

# Include all web assets and handle asset subdirectories cleanly
source.include_exts = py, png, jpg, jpeg, kv, atlas, html, css, js
source.include_patterns = www/*, assets/*, www/assets/*

version = 1.0.0
requirements = python3, kivy, android, pyjnius

orientation = portrait
fullscreen = 1
icon.filename = icon.png

# Android Specific Target Configuration
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.enable_androidx = True
android.archs = arm64-v8a, armeabi-v7a
android.target = aab

# Cleartext permissions allow loading internal HTTP data if needed
android.manifest.application_attributes = android:usesCleartextTraffic="true"
android.permissions = INTERNET, ACCESS_NETWORK_STATE

[buildozer]
log_level = 2
warn_on_root = 1
