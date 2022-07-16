@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\BootIce.7z
@7z.exe x -o"%TEMP%\HBCD" -y Files\WinNTSetup.7z
@start "" /D"%TEMP%\HBCD" "WinNTSetup.exe"