Option Explicit

Dim opcion, segundos

opcion = InputBox("¿Cuándo querés que se apague el equipo?" & vbCrLf & _
                  "1 - 1 hora" & vbCrLf & _
                  "15 - 15 minutos" & vbCrLf & _
                  "30 - 30 minutos" & vbCrLf & _
                  "45 - 45 minutos" & vbCrLf & _
                  "s - Cancelar apagado programado", _
                  "Temporizador de Apagado")

If opcion = "1" Then
    segundos = 3600
ElseIf opcion = "15" Then
    segundos = 900
ElseIf opcion = "30" Then
    segundos = 1800
ElseIf opcion = "45" Then
    segundos = 2700
ElseIf LCase(opcion) = "s" Then
    Cancelar
    MsgBox "El apagado programado fue cancelado.", vbInformation, "Cancelado"
    WScript.Quit
Else
    MsgBox "Opción inválida. Debés escribir 1, 15, 30, 45 o 's'.", vbExclamation, "Error"
    WScript.Quit
End If

Dim confirm
confirm = MsgBox("¿Seguro que querés programar el apagado en " & segundos/60 & " minutos?", vbYesNo + vbQuestion, "Confirmar")
If confirm = vbYes Then
    Apagar segundos
Else
    MsgBox "Acción cancelada.", vbInformation, "Cancelado"
End If

' === FUNCIONES ===

Sub Apagar(segundos)
    Dim shell
    Set shell = CreateObject("WScript.Shell")
    shell.Run "shutdown -s -f -t " & segundos & " -c ""El sistema se apagará automáticamente en " & segundos/60 & " minutos."""
End Sub

Sub Cancelar()
    Dim shell
    Set shell = CreateObject("WScript.Shell")
    shell.Run "shutdown -a"
End Sub
