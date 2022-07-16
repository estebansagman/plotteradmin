@pushd "%~dp0"
@if not exist "%TEMP%\HBCD\regrepair.exe" 7z.exe x -o"%TEMP%\HBCD" -y Files\GlaryRegistryRepair.7z
@start "" /D"%TEMP%\HBCD" "regrepair.exe"