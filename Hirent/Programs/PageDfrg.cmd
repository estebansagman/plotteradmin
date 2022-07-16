@pushd "%~dp0"
@7z.exe e -o"%TEMP%\HBCD" -y Files\Sysinternals.7z PageDfrg.exe
@start "" /D"%TEMP%\HBCD" "PageDfrg.exe" /accepteula