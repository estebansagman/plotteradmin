@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z myuninst.exe
@start "" /D"%TEMP%\HBCD" "myuninst.exe"