... import os
... import shutil
... import requests
... 
... # Function to download file from url
... def download_file(url, save_path):
...     with requests.get(url, stream=True) as r:
...         with open(save_path, 'wb') as f:
...             shutil.copyfileobj(r.raw, f)
... 
... # Discord download URL for Windows
... discord_url = "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64"
... 
... # Set download path to Downloads folder
... download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
... os.makedirs(download_folder, exist_ok=True)
... 
... # Filename to save as (Discord installer)
... filename = "discord_installer.exe"
... installer_path = os.path.join(download_folder, filename)
... 
... # Download Discord installer
... print(f"Downloading Discord installer from {discord_url} to {installer_path}...")
... download_file(discord_url, installer_path)
... print("Download complete.")
... input('Press ENTER to exit')
