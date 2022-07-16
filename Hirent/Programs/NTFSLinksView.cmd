@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y Files\NirSoft.7z NTFSLinksView.exe
@start "" /D"%TEMP%\HBCD" "NTFSLinksView.exe"