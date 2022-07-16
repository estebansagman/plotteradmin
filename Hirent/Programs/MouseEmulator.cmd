@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z mousem*
@start "" /D"%TEMP%\HBCD" "mousemu.exe"
@type "%TEMP%\HBCD\mousem.txt"
@pause>nul