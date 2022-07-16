@pushd "%~dp0"
@if not exist "%TEMP%\HBCD\WirelessKeyView.exe" 7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z WirelessKeyView.exe
@start "" /D"%TEMP%\HBCD" "WirelessKeyView.exe"