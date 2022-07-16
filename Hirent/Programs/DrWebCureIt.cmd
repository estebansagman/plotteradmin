@echo off
pushd "%~dp0"
title DrWebCureIt
echo DrWebCureIt Antivirus
if "%COMPUTERNAME:~0,6%"=="MiniXP" echo Hint: Do NOT choose EPM in the next screen
echo.
echo  1. Start (Press ENTER)
echo  2. Download updated version
echo.
set /p upd=Choose an option : 
if not "%upd%"=="2" goto s
7z.exe x -o"%TEMP%\HBCD" -y Files\Mix.7z download.exe
cd /d "%TEMP%\HBCD"
download.exe ftp://ftp.drweb.com/pub/drweb/cureit/cureit.exe /output:DrWebCureIt.exe /display:progress /overwrite
:s
start "" DrWebCureIt.exe