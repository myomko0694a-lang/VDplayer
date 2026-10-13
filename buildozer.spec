[app]

# (str) Title of your application
title = VDPlayer

# (str) Package name
package.name = vdplayer

# (str) Package domain (needed for android packaging)
package.domain = org.vplayer

# (str) Source files where the *.py files exist
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,kivymd,certifi

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android build tools version
android.build_tools_version = 33.0.0

# (str) Android APK versioning
version = 1.0

[buildozer]
log_level = 2
