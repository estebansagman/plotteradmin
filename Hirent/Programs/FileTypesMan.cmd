@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z FileTypesMan.exe
@start "" /D"%TEMP%\HBCD" "FileTypesMan.exe"