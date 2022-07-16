@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD\Avira" -y Files\AviraAntiVir.7z
@7z.exe x -o"%TEMP%\HBCD\Avira" -y Files\Mix.7z download.exe
@copy /y 7z.* "%TEMP%\HBCD\Avira">nul
@if not exist %SystemRoot%\System32\msvcr71.dll 7z.exe x -o"%TEMP%\HBCD\Avira" -y Files\DLL.7z ms*71.dll
@start "" /D"%TEMP%\HBCD\Avira" "AviraScan.cmd"