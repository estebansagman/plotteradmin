@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z Shredder.exe
@start "" /D"%TEMP%\HBCD" "Shredder.exe"