@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Piriform.7z r*
@start "" /D"%TEMP%\HBCD" "recuva.exe"