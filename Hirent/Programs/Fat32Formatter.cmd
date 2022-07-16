@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z guiformat.exe
@start "" /D"%TEMP%\HBCD" "guiformat.exe"