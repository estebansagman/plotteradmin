@pushd "%~dp0"
@7z.exe x -o"%TEMP%\HBCD\DeviceDoctor" -y Files\DeviceDoctor.7z
@7z.exe x -o"%TEMP%\HBCD\DeviceDoctor\Microsoft.VC90.CRT" -y Files\DLL.7z msvcr90.dll
@start "" /D"%TEMP%\HBCD\DeviceDoctor" "DeviceDoctor.exe"