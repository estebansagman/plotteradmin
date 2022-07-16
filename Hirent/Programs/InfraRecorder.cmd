@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\InfraRecorder.7z
@7z.exe x -o"%TEMP%\HBCD\cdrtools" -y Files\mkisofs.7z
@start "" /D"%TEMP%\HBCD" "InfraRecorder.exe"