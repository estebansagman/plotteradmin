@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z BlueScreenView.exe
@start "" /D"%TEMP%\HBCD" "BlueScreenView.exe"