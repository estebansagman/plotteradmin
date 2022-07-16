@echo off
pushd "%~dp0"
7z.exe x -o"%TEMP%\HBCD" -y ..\Dos\PCI32.7z
cd /d "%TEMP%\HBCD"
"%TEMP%\HBCD\PCI32.exe"
"%TEMP%\HBCD\PCI32.exe" > "%TEMP%\HBCD\PCI32.txt"
start "" "%TEMP%\HBCD\PCI32.txt"
echo. Press any key to exit.
pause>nul