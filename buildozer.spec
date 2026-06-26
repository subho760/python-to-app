[app]
title = Dragon Hole
package.name = dragonhole
package.domain = org.nightshadow
source.dir = .
source.include_exts = py, png, jpg, jpeg, html, css, js
source.include_patterns = web/*

version = 1.0.0
requirements = python3, kivy, android, pyjnius
orientation = portrait
fullscreen = 1
icon.filename = icon.png

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.enable_androidx = True
android.archs = arm64-v8a, armeabi-v7a
android.target = aab

android.manifest.application_attributes = android:usesCleartextTraffic="true"
android.permissions = INTERNET, ACCESS_NETWORK_STATE

[buildozer]
log_level = 2
warn_on_root = 1
