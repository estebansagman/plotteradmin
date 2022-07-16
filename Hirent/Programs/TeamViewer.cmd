@pushd "%~dp0"
@if not exist "%TEMP%\HBCD\TeamViewer.exe" 7z.exe e -o"%TEMP%\HBCD" -y Files\TeamViewer.7z
@start "" /D"%TEMP%\HBCD" "TeamViewer.exe"