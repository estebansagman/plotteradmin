@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z AlternateStreamView.exe
@start "" /D"%TEMP%\HBCD" "AlternateStreamView.exe"