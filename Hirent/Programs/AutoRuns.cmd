@pushd "%~dp0"
@7z.exe e -o"%TEMP%\HBCD" -y Files\Sysinternals.7z Autoruns.exe
@REG ADD HKCU\Software\Sysinternals\Autoruns /v EulaAccepted /t REG_DWORD /d 1 /f
@start "" /D"%TEMP%\HBCD" "autoruns.exe"