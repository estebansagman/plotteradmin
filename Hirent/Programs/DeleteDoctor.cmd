@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z deletedr.exe
@start "" /D"%TEMP%\HBCD" "deletedr.exe"