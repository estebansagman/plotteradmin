@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z regbak.exe
@start "" /D"%TEMP%\HBCD" "regbak.exe" 