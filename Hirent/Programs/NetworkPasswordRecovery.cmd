@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z netpass.exe
@start "" /D"%TEMP%\HBCD" "netpass.exe"