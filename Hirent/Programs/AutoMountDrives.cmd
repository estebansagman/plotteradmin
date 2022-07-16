@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\AutoMountDrives.7z
@start "" /D"%TEMP%\HBCD" "AutoMountDrives.exe"