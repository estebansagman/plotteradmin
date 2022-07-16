@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z dev* fix*
@start "" /D"%TEMP%\HBCD" "fix_hdc.cmd"