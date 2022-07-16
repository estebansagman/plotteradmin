@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z KeyTweak.exe
@start "" /D"%TEMP%\HBCD" "KeyTweak.exe"