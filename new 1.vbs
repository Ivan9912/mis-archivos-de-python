atrMessage =InputBox("Enter Password","Se requiere Contrase�a","Escriba Aqu�")
if atrMessage = "1595" then
    msgbox "Contrase�a conrrecta"
	set variable = createobject("WScript.Shell")
	variable.Run "https://www.youtube.com/watch?v=VGVFigJYGOc"
else
    msgbox "Contrase�a incorrecta"
end if