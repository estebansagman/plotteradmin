@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z SpaceMonger.exe
@start "" /D"%TEMP%\HBCD" "SpaceMonger.exe"