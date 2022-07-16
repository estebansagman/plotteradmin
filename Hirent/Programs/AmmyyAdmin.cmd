@pushd "%~dp0"
@if not exist "%TEMP%\HBCD\AMMYY_Admin.exe" 7z.exe x -o"%TEMP%\HBCD" -y Files\AmmyyAdmin.7z
@start "" /D"%TEMP%\HBCD" "AMMYY_Admin.exe"