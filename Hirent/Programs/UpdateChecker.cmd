@pushd "%~dp0"
@if "%COMPUTERNAME:~0,6%"=="MiniXP" echo This program does not work from MiniXP&echo You can run it from your installed Windows XP/Vista/7&pause
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z UpdateChecker.exe
@start "" /D"%TEMP%\HBCD" "UpdateChecker.exe"