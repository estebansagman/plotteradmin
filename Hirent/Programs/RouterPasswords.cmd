@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z RouterPasswords.html
@start "" /D"%TEMP%\HBCD" "RouterPasswords.html"