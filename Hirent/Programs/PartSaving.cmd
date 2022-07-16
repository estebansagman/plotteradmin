@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y ..\Dos\SavePart.7z
@start "" /D"%TEMP%\HBCD" "spartwin.exe"