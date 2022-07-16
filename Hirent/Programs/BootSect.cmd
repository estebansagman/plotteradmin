@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\BootSect.7z
@cd /d "%TEMP%\HBCD"
@BootSect.exe /help>BootSect.txt
@start "" "%TEMP%\HBCD\BootSect.txt"
@cmd /k "%TEMP%\HBCD\BootSect.exe"