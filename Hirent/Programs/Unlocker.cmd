@echo off
pushd "%~dp0"
if exist "%TEMP%\HBCD\UnlockerAssistant.exe" goto s
7z.exe x -o"%TEMP%\HBCD" -y Files\unlocker.7z
if defined ProgramFiles(x86) (copy /y "%TEMP%\HBCD\x64\*.*" "%TEMP%\HBCD")
:s
start "" /D"%TEMP%\HBCD" "UnlockerAssistant.exe"
echo Unlocker Assistant is running in System Tray,
echo Now you can try to delete a Locked item.
echo.
echo Press any key to EXIT
pause>nul