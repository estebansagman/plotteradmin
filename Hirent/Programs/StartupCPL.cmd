@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z startupc.exe
@start "" /D"%TEMP%\HBCD" "startupc.exe"