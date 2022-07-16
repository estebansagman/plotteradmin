@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z RegFromApp.exe
@start "" /D"%TEMP%\HBCD" "RegFromApp.exe"