[app]
title = WebWrapperPro
package.name = webwrapperpro
package.domain = org.subho.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js
version = 1.0.0

requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.allow_backup = True

# Target Android 13 (API 33)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Native Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Resource Configuration
# We include 'web' in source.include_dirs to ensure it's packaged
source.include_dirs = web

[buildozer]
log_level = 2
warn_on_root = 1
