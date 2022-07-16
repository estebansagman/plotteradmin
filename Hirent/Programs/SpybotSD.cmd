@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD\SpybotSD" -y Files\SpybotSD.7z
@REG ADD "HKCU\Software\Safer Networking Limited\SpybotSnD" /v WizardRun /t REG_DWORD /d 1 /f
@start "" /D"%TEMP%\HBCD\SpybotSD" "SpybotSD.exe"