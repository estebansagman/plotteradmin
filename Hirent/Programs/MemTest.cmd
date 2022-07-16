@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z memtest.exe
@start "" /D"%TEMP%\HBCD" "memtest.exe"