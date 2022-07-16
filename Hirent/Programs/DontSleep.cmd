@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z DontSleep.exe
@start "" /D"%TEMP%\HBCD" "DontSleep.exe"