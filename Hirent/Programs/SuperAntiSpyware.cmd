@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD\SuperAntiSpyware" -y Files\SuperAntiSpyware.7z
@7z.exe x -o"%TEMP%\HBCD\SuperAntiSpyware" -y Files\DLL.7z msvcr71.dll
@start "" /B /D"%TEMP%\HBCD\SuperAntiSpyware" "startSAS.cmd"