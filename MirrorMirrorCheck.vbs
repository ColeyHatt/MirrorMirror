result = MsgBox ("Do you want to stay on this page?", vbYesNo, "Do you want to stay on this page?")

Dim oShell : Set oShell = CreateObject("WScript.Shell")
Select Case result
Case vbYes

Case vbNo
    oShell.Run "taskkill /f /im Steam.exe"
    oShell.Run "taskkill /f /im notepad++.exe"
    oShell.Run "taskkill /f /im chrome.exe"
End Select
