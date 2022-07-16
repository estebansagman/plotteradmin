@pushd "%~dp0"
@for %%x in (NT6xFastInstaller GImageX BootSect) do 7z.exe x -o"%TEMP%\HBCD" -y Files\%%x.7z
@start "" /D"%TEMP%\HBCD" "installer.cmd"