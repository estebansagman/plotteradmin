@pushd "%~dp0"
@7z.exe e -o"%TEMP%\HBCD" -y Files\Piriform.7z c* w*
@start "" /D"%TEMP%\HBCD" "CCleaner.exe"