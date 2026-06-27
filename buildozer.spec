[app]
title = Dragon Hole
package.name = dragonhole
package.domain = org.nightshadow
source.dir = .
source.include_exts = py, png, jpg, jpeg

version = 1.0.0
requirements = python3, kivy

orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.enable_androidx = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
