@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z RemoveWGA.exe
@start "" /D"%TEMP%\HBCD" "RemoveWGA.exe"