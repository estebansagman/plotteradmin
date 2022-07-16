@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z mspass.exe
@start "" /D"%TEMP%\HBCD" "mspass.exe"