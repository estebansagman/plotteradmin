@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z IsMyLcdOK.*
@start "" /D"%TEMP%\HBCD" "IsMyLcdOK.exe"