@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z RegShot.exe
@start "" /D"%TEMP%\HBCD" "RegShot.exe"