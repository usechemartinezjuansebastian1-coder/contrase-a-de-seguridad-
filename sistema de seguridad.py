print ("sistema de seguridad")

contraseña = "1234"
fallidos = 0
admin = input ("ingrese la contraseña del administrador de 4 digitos:")

while admin != contraseña:
    fallidos = fallidos + 1
    print (f"contraseña incorrecta, intento fallido #{fallidos}.")
    if fallidos == 3:
        print ("demasiados intentos fallidos, cierre del sistema.")
        break
    admin = input ("ingrese la contraseña del administrador:")
if admin == contraseña:
    print ("acceso concedido, bienvenido al sestema de seguridad.")