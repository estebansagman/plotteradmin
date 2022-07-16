@pushd "%~dp0"
@7z.exe e -o"%TEMP%\HBCD" -y Files\Sysinternals.7z RegMon.exe
@REG ADD HKCU\Software\Sysinternals\RegMon /v EulaAccepted /t REG_DWORD /d 1 /f
@start "" /D"%TEMP%\HBCD" "RegMon.exe"