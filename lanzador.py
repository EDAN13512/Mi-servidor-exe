import os
import sys

# Parche para errores de DLL en Windows 7
if sys.platform == 'win32':
    import ctypes
    try:
        ctypes.windll.kernel32.SetDllDirectoryW(None)
    except:
        pass

import uploadserver

if __name__ == '__main__':
    port = 8000
    print(f"Servidor iniciado en: http://localhost:{port}")
    print("Para subir: /upload")
    try:
        uploadserver.main(port=port)
    except Exception as e:
        print(f"Error al iniciar: {e}")
        input("Presiona Enter para salir...")
