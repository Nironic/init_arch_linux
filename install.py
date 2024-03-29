import os
red = "\033[91m"
green = "\033[92m"
blue  = "\033[94m"

def run(com):
    res = os.system(com)
    return res

def log(text, info):
    if info == "i":
        print(blue + "[INFO]: " + text + "\033[0m")
    if info == "c":
        print(green + "[COMPLETE]: " + text + "\033[0m")
    if info == "e":
        print(red + "[ERROR]: " + text + "\033[0m")

def install(pack):
    for i in pack:
        log("Установка " + i + "..", "i")
        res = run("sudo pacman -S " + i)
        if res == 0:
            log("Установка пакета " + i + " прошла успешно.", "c")
        else:
            log("Установка пакета " + i + " завершена с ошибкой.", "e")

def KDE(coms):
    error = 0
    for i in coms:
        res = run(i)
        if res != 0:
            error += 1
    return error

def Gchrome():
    log("Установка AUR для загрузки браузера.")
    install(["base-devel", "git"])
    log("Установка компонентов браузера Google Chrome.", "i")
    res = KDE(["git clone https://aur.archlinux.org/yay-git.git", "cd yay-git && makepkg -si"])
    if res == 0:
        log("Установка компонентов успешно завершена.", "c")
    else:
        log("Установка Google Chrome компонентов произошла ошибка.", "e")
        break
    log("Установка Google Chrome..", "i")
    res = run("yay -S google-chrome")
    if res == 0:
        log("Google Chrome успешно установлен.", "c")
    else:
        log("Google Chrome не установлен.", "e")

def teleinstall():
    log("Установка Telegramm.", "i")
    res = run("sudo pacman -S telegram-desktop")
    if res == 0:
        log("Telegramm успешно установлен.")
    else:
        log("В установке Telegramm произошла ошибка.", "e")

def setting_pip():
    log("Настройка pip.", "i")
    user = os.getlogin()
    run("mkdir /home/" + str(user) + "/pip")
    file = open("/home/" + user + ".config/pip/pip.conf", "w")
    file.write("[global]\nbreak-system-packages = true")
    file.close()
    log("Pip успешно настроен", "c")

def pacmans():
    log("Настройка Pacman.", "i")
    file = open("/etc/pacman.conf", "r")
    info = file.read()
    file.close()
    info = info.replace("#ParallelDownloads = 5", "ParallelDownloads = 10")
    file = open("etc/pacman.conf", "w")
    file.write(info)
    file.close()
    log("Pacman успешно настроен.", "c")

def optimizate():
    log("Установка пакетов для оптимизации системы. [Шаг 1]", "i")
    error = KDE(["git clone https://aur.archlinux.org/ananicy.git", "cd ananicy && makepkg -sric", "sudo systemctl enable --now ananicy"])
    if error == 0:
        log("[Шаг 1]: Успешно", "c")
    else:
        log("[Шаг 1]: Произошла ошибка", "e")
    log("Установка пакетов для оптимизации системы. [Шаг 2]", "i")
    res = run("sudo pacman -S haveged")
    if res == 0:
        log("Пакет оптимизации успешно установлен. [Шаг 2]", "c")
        log("Запуск службы.", "i")
        res = run("sudo systemctl enable haveged")
        if res == 0:
            log("Служба оптимизации успешно запущена. [Шаг 2]", "c")
        else:
            log("Служба оптимизации не запущена. [Шаг 2]", "e")
    else:
        log("Пакет оптимизации не установлен. [Шаг 2]", "e")
    
    log("Установка пакетов для оптимизации системы. [Шаг 3]", "i")
    res = run("sudo pacman -S cpupower")
    if res == 0:
        log("Пакет оптимизации успешно установлен. [Шаг 2]", "c")
        log("Запуск службы.", "i")
        #run("echo governor=\"performance\" >> /etc/default/cpupower")
        run("sudo cpupower frequency-set -g performance")
        res = run("sudo systemctl enable cpupower")
        if res == 0:
            log("Служба оптимизации успешно запущена. [Шаг 2]", "c")
        else:
            log("Служба оптимизации не запущена. [Шаг 2]", "e")
    else:
        log("Пакет оптимизации не установлен. [Шаг 2]", "e")
    
    

log("Модули импортированы.", "c")
pacmans()
log("Обновление системы..", "i")
res = run("sudo pacman -Syu")
if res == 0:
    log("Обновление системы успешно завершена.", "c")
else:
    log("Обновление системы не произведено.", "e")
log("Запуск установки Bluez и Bluez-utils (Для полноценной работы bluetooth драйвера)", "i")
install(["bluez", "bluez-utils"])
log("Настройка и запуск bluetooth.", "i")
res = run("systemctl start bluetooth.service")
if res == 0:
    log("Bluetooth настроен и запущен.", "c")
else:
    log("Bluetooth не настроен. Запуск не может быть произведён.")
Gchrome()
teleinstall()
setting_pip()
optimizate()
log("Установка ПО завершена.", "c")
