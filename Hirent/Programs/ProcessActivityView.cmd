@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z ProcessActivityView.exe
@start "" /D"%TEMP%\HBCD" "ProcessActivityView.exe"