[app]
title = Yashod
package.name = yashod
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,opencv-python,gTTS,pygame,pillow,setuptools
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 26b
android.entrypoint = org.kivy.android.PythonActivity
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.debug_artifact = apk
android.release_artifact = aab

[buildozer]
log_level = 2
warn_on_root = 1

0