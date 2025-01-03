import os

def install_yay():
    os.system("sudo pacman -Syuu --noconfirm")
    os.system("sudo pacman -S --needed base-devel git --noconfirm")
    os.system("git clone git clone https://aur.archlinux.org/yay.git")
    os.system("cd yay && makepkg -si --noconfirm")
    os.system("sudo yay -Syuu --noconfirm")

def install(pack):
    os.system("yay -Syuu --noconfirm --needed " + pack)

def hyprland():
    os.system("cp -r hypr ~/.config/")

def locale():
    tm = "ru_RU.UTF-8 UTF-8"
    file1 = open("/etc/locale.gen", "r")
    data = file1.read()
    file1.close()
    data = data + "\n" + tm
    file1 = open("/etc/locale.gen", "w")
    file1.write(data)
    file1.close()
    os.system("sudo locale-gen")

def install_theme():
    os.system("git clone https://github.com/vinceliuice/Graphite-gtk-theme")
    os.system("cd Graphite-gtk-theme && ./install")


def fish():
    fl = open("~/.config/fish/config.fish", "w")
    fl.write("if status is-interactive\n    export XDG_CURRENT_DESKTOP=Hyprland\n   export XDG_SESSION_TYPE=wayland\n   fastfetch\nend")
    fl.close()
    print("/bin/fish")
    os.system("chsh")

command = """
sudo systemctl enable fstrim.timer
sudo systemctl enable bluetooth
sudo systemctl enable --now ananicy
sudo systemctl enable sddm
"""

install_yay()
fl = open("packet.data", "r")
data = fl.read()
fl.close()

for i in data.split("\n"):
    if i != "":
        install(i)

hyprland()
locale()
install_theme()
fish()

for i in command.split("\n"):
    os.system(i)
