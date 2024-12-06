import os
import sys
import subprocess

def execute_warp_command(command):
    warp_cli_path = r"C:\Progra~1\Cloudflare\Cloudflare WARP\warp-cli.exe"
    if not os.path.exists(warp_cli_path):
        print("Error: warp-cli not found in the expected directory.")
        sys.exit(1)

    try:
        # Ejecutar el comando warp-cli con el argumento proporcionado
        result = subprocess.run([warp_cli_path, command], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e.stderr)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python warpcli.py -c <warp-cli command>")
        sys.exit(1)
    
    command = sys.argv[2]
    execute_warp_command(command)
