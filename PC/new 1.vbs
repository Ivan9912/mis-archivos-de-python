atrMessage =InputBox("Enter Password","Se requiere ContraseÃ±a")

if atrMessage = "1595" then
    msgbox "Contraseña conrrecta"
	set variable = createobject("WScript.Shell")
	variable.Run "https://www.youtube.com/watch?v=VGVFigJYGOc"
        variable.Run "http://www.pythontutor.com/visualize.html#code=Cantidad_I%20%3D%20%5B%5D%0AREG_DISTANCIAS%20%3D%20%5B%5D%0A%0ADIST_Xo%20%3D%201%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23Metros%0AVEL_V%20%3D%205%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23Mts/seg.%0ATIEMPO_T%3D%2015%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23Seg.%0A%0Adef%20X_FINAL%20%28X,%20V,%20T%29%3A%0A%20%20%20%20I%20%3D%200%0A%20%20%20%20while%20I%20%3C%3D%20T%3A%0A%20%20%20%20%20%20%20%20Cantidad_I.append%20%28I%29%0A%20%20%20%20%20%20%20%20POS_FINAL%20%3D%20%2830%20%2B%20V%20*%20I%29%0A%20%20%20%20%20%20%20%20REG_DISTANCIAS.append%20%28POS_FINAL%29%0A%20%20%20%20%20%20%20%20I%3DI%2B1%0A%20%20%20%20return%20POS_FINAL%0A%20%20%20%20%0AFINAL%20%3D%20X_FINAL%20%28DIST_Xo,%20VEL_V,%20TIEMPO_T%29%0Aprint%20%28%22Posici%C3%B3n%20X%28t%29%3A%22,%20FINAL,%22Metros.%20En%22,%20TIEMPO_T,%22Segundos.%22%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"
else
    msgbox "Contraseña incorrecta"
end if