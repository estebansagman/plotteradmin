@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD" -y ..\Dos\MBRUtil.7z
@cd /d "%TEMP%\HBCD"
@start "" "mbr.txt"
@ren mbrw.exe mbr.exe
@start "mbr.exe" /D"%TEMP%\HBCD" "cmd.exe" /k mbr.exe