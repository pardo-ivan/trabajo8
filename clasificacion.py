import os
import shutil

# Ruta base (la carpeta donde están los logs)
# Ruta base: usa tu carpeta exacta
base_path = (r"C:/Users/ialbornoz/OneDrive - Subsecretaría para las Fuerzas Armadas/Escritorio/ALLSAFE_logs/")


# Carpetas destino
folders = {
    '_app_1.txt': 'logs_app_1',
    '_app_2.txt': 'logs_app_2',
    '_app_3.txt': 'logs_app_3',
}

# Crear carpetas si no existen
for folder in folders.values():
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Recorrer los archivos en la carpeta base
for file in os.listdir(base_path):
    file_path = os.path.join(base_path, file)

    if os.path.isfile(file_path):
        for ext, folder in folders.items():
            if file.endswith(ext):
                dest = os.path.join(base_path, folder, file)
                shutil.move(file_path, dest)
                print(f"Movido: {file} → {folder}")
                break

print("\nClasificación completada.", )
