import os

def __install__():
    os.system("sudo pacman -Syuu --noconfirm")
    os.system("sudo pacman -Syuu python python-pip --noconfirm")
    os.system("pip install colorama --break-system-packages")

def __install__yay__():
    os.system("sudo pacman -S --needed base-devel git --noconfirm")
    os.system("cd yay && makepkg -si --noconfirm")
    os.system("sudo yay -Syuu --noconfirm")

def install(pack):
    os.system("sudo yay -Syuu --noconfirm " + pack)


packet = ["ananicy", "google-chrome", "portproton", "visual-studio-code-bin", "mesa", "lib32-mesa", "vulkan-radeon", "lib32-vulkan-radeon", "vulkan-icd-loader", "lib32-vulkan-icd-loader", "vlc", "ardour", "telegram-desktop-bin", "steam", "bluez", "bluez-deprecated-tools", "shadowsocks"]

def vpn():
    os.system("mkdir -p /home/nironic/AutoStart/vpn")
    
    start = """
#!/bin/bash
/usr/bin/sslocal -c /home/nironic/AutoStart/vpn/profile.json
    """

    units= """
[Unit]
Description=Vpn
After=default.target

[Service]
ExecStart=/home/nironic/AutoStart/vpn/start.sh
Restart=always  # Перезапускать при сбое

[Install]
WantedBy=default.target
    """
    profile = """
{
    "server": "89.46.238.103",
    "server_port": 443,
    "local_port": 1080,
    "password": "1IlfUya1mXeyVAbMmurzzq",
    "method": "chacha20-ietf-poly1305"
}
    """
    st = open("/home/nironic/AutoStart/vpn/start.sh", "w")
    st.write(start)
    st.close()
    os.system("mkdir -p /home/nironic/.config/systemd/user")
    unit = open("/home/nironic/.config/systemd/user/vpn.service", "w")
    unit.write(units)
    unit.close()
    pr = open("/home/nironic/AutoStart/vpn/profile.json", "w")
    pr.write(profile)
    pr.close()
    os.system("systemctl --user enable vpn.service")

__install__()
__install__yay__()
for i in packet:
    install(i)

#Command
#Trim
def run(com):
    os.system(com)

command = """
sudo systemctl enable fstrim.timer
sudo systemctl enable bluetooth
sudo systemctl enable --now ananicy
sudo fstrim -v /
"""
for i in command.split("\n"):
    run(i)

vpn()