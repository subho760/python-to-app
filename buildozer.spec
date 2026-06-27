[app]
title = KivyColorApp
package.name = kivycolorapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Android API & NDK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_path = 
android.sdk_path = 
android.accept_sdk_license = True

# Build options
android.logcat_filters = *:S python:D
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
