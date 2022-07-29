import os
import requests
from os import path

response = requests.get("http://setup.roblox.com/version")
vers = response.text

print("Roblox version: " + vers)

def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = url.split('/')[-1].replace(" ", "_")
    file_path = os.path.join(dest_folder, filename)

    print("Downloading oof sound...")
    r = requests.get(url, stream=True)
    print("Downloaded.")

    if r.ok:
        print("Saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))

p = ""
if path.isdir("C:/Program Files (x86)/Roblox"):
    p = os.path.join("C:/Program Files (x86)/Roblox/Versions/", vers, "content", "sounds")
else:
    p2 = path.expandvars(r'%LOCALAPPDATA%') 
    p2 = p2 + "/"
    p = os.path.join(p2, "Roblox", "Versions", vers, "content", "sounds")

download("https://cdn.discordapp.com/attachments/963908857082544138/1001625905984180315/ouch.ogg", dest_folder=p)
print("Done.")
os.system("pause")