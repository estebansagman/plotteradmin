@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD\IPScanner" -y Files\Mix.7z ipscan.exe
@start "" /D"%TEMP%\HBCD\IPScanner" "ipscan.exe"