@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z RegScanner.exe
@start "" /D"%TEMP%\HBCD" "RegScanner.exe"