set WshShell = WScript.CreateObject("WScript.Shell")
WScript.Sleep 10000
WshShell.Run ("""C:\Administracion\1024.bat""")
WScript.Sleep 500

WshShell.Run "cmd.exe" 
WScript.Sleep 500
WshShell.SendKeys "taskkill /f /im explorer.exe"
WScript.Sleep 500
WshShell.SendKeys "{ENTER}"
WScript.Sleep 1000
WshShell.SendKeys "iniciarPlot"
WScript.Sleep 500
WshShell.SendKeys "{ENTER}"

WScript.Sleep 500
WshShell.Run ("""C:\Administracion\CoreTemp.exe""")
WScript.Sleep 500
WshShell.Run ("""C:\Administracion\control.py.txt""")








