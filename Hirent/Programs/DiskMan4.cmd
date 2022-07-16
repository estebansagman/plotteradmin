@pushd "%~dp0"
@7z.exe e -o"%TEMP%\HBCD" -y ..\Dos\biosboot.7z d*
@cd /d "%TEMP%\HBCD"
@echo.|diskman4.exe>diskman4.txt
@start "" "%TEMP%\HBCD\diskman4.txt"
@start "diskman4.exe" /D"%TEMP%\HBCD" "cmd.exe /k "%TEMP%\HBCD\diskman4.exe"
@pause