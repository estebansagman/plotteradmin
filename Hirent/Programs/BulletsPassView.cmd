@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z BulletsPassView.exe
@start "" /D"%TEMP%\HBCD" "BulletsPassView.exe"