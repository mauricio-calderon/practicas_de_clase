usuarios = []
for i in range(50):
    usuarios.append(
        {
            'usuario': f"Usuario {i}",
            'nombre': f"Nombre {i}",
            'contrasena': f"Contrasena {i}",
        }
    )

for usuario in usuarios:
    print(usuario)