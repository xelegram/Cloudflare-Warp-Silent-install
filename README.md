# **Warp Silent Install on Windows**

This repository contains a Python script to silently download, install, and configure the **Cloudflare WARP** client on Windows systems.

## **Features**
- Automatically downloads the installation file from a specified URL.
- Renames the downloaded file from `.zip` to `warp.msi`.
- Installs the WARP client silently using `msiexec`.
- Automatically terminates the Cloudflare WARP GUI process after installation.

## **Requirements**
- **Python 3.x** installed on your system.
- Administrator privileges to install software and manage processes.
- `msiexec` (It comes by default in Windows).

## **Usage**
1. Clone this repository or download the `install_warp.py` script:
   ```bash
   git clone https://github.com/xelegram/Cloudflare-Warp-Silent-install.git
   cd warp-silent-install


2. Install Warp silently
   ```bash
   python3 install_warp.py

## **Silent Commands (Optional)**
1. Register the device
   ```bash
      python warpcli.py -c register
2. Connect device to warp network
   ```bash
   python warpcli.py -c connect

Others
   ```bash
   python warpcli.py -c disconnect
```
Other commands
Operation Mode Configuration
   warpcli.py -c set-mode warp

Switch to WARP+ mode (if you have a premium account).
   warpcli.py -c set-mode warp+doh

Configure WARP to use DNS over HTTPS (DoH) exclusively.
   warpcli.py -c set-mode doh

Switch to DNS over HTTPS only mode, without VPN.
   warpcli.py -c get-mode

Show the current WARP mode.
5. Connection Configuration
   warpcli.py -c enable-proxy

Enable proxy mode so other applications can use WARP through a proxy.
   warpcli.py -c disable-proxy

Disable proxy mode.
   warpcli.py -c enable-dns-log

Enable DNS query logging for debugging.
   warpcli.py -c disable-dns-log

Disable DNS query logging.
