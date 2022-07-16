@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z NTFSAccess.*
@start "" /D"%TEMP%\HBCD" "NTFSAccess.exe"