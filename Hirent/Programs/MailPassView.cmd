@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z mailpv.exe
@start "" /D"%TEMP%\HBCD" "mailpv.exe"