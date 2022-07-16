@pushd "%~dp0"
@if not exist "%TEMP%\HBCD\Opera\Opera.exe" 7z.exe x -o"%TEMP%\HBCD\Opera" -y Files\Opera.7z
@start "" /Max /D"%TEMP%\HBCD\Opera" "Opera.exe" %*
@exit