atrMessage =InputBox("Enter Password","Se requiere Contraseña","Escriba Aquí")
if atrMessage = "1595" then
    msgbox "Contraseña conrrecta"
	set variable = createobject("WScript.Shell")
	variable.Run "https://www.youtube.com/watch?v=VGVFigJYGOc"
else
    msgbox "Contraseña incorrecta"
end if