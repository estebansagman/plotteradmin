@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z smsniff.exe
@start "" /D"%TEMP%\HBCD" "smsniff.exe"