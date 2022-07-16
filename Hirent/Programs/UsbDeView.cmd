@pushd "%~dp0"
@if not exist "%TEMP%\HBCD\usbdeview.exe" 7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z usbdeview.exe
@start "" /D"%TEMP%\HBCD" "usbdeview.exe"