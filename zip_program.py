import os
import zipfile
import configparser
import re
from random import randint
from datetime import datetime
from PIL import Image

months = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}


def ls_l(archivePath, path_file, vremen):
    Path = zipfile.Path(archivePath, path_file)
    with zipfile.ZipFile(archivePath, mode="r") as archive:
        for i in Path.iterdir():
            file = path(str(i.name), path_file, archivePath)
            info = archive.getinfo(file)
            mon_ = months[info.date_time[1]] + "\t" + str(info.date_time[2]) + " " + str(info.date_time[3]).rjust(2, "0") + ":" + str(info.date_time[4]).rjust(2, "0")
            if file in vremen:
                mon_ = vremen[file]
            rasmer = info.file_size
            prava = "-rw-r--r--"
            if info.is_dir():
                rasmer = randint(200, 1800)
                prava = "drwxr-xr-x"
            print(f'{prava} {randint(1, 5)} Antua Antua {rasmer} {mon_} {i.name}')


def ls(archivePath, path_file):
    Path = zipfile.Path(archivePath, path_file)
    count = 0
    for i in Path.iterdir():
        count += len(i.name)
        if count > 45:
            count = 0
            print(i.name)
        else:
            print(i.name, end='\t')
    if count != 0:
        print()
    return ([i.name for i in Path.iterdir()])


def path(command, path_file, archivePath):
    if not command.startswith('\\'):  # не по абсолютному пути
        command = path_file + command
    else:
        command = command[1:]
    norm_path = str(os.path.normpath(command)).replace('\\', '/') # на винде работает программа
    if norm_path == '.':  # может быть пустым
        return ''
    Path = zipfile.Path(archivePath, norm_path)
    if Path.is_file() and Path.exists():  # файл
        return norm_path
    Path = zipfile.Path(archivePath, norm_path + '/')
    norm_path = norm_path + '/'
    if Path.is_dir() and Path.exists():
        return norm_path
    return '*'  # не нашёл ничего


def cd(command, path_file, archivePath):
    result = path(command, path_file, archivePath)
    if result == '*':
        print(f"bash: cd: {command}: No such file or directory")
        return path_file
    Path = zipfile.Path(archivePath, result)
    if Path.is_file() and Path.exists():
        print(f"bash: cd: {Path.name}: Not a directory")
        return path_file
    return result


def touch(command, path_file, archivePath, vremen):
    if not command.startswith('\\'):  # не по абсолютному пути
        command = path_file + command
    else:
        command = command[1:]
    norm_path = str(os.path.normpath(command)).replace('\\', '/') # на винде работает программа
    # c самим файлом
    Path = zipfile.Path(archivePath, os.path.dirname(norm_path) + '/') # c его потомком-папкой
    if not os.path.dirname(norm_path) or (Path.is_dir() and Path.exists()):
        with zipfile.ZipFile(archivePath, 'a') as myzip:
            Path = zipfile.Path(archivePath, norm_path)
            if not Path.exists():
                myzip.writestr(norm_path, "")
            else:
                current_time = datetime.now()
                formatted_time = current_time.strftime("%b\t%d %H:%M")
                vremen[norm_path] = formatted_time


def wc(command, path_file, archivePath):
    wc_path = path(command, path_file, archivePath)
    Path = zipfile.Path(archivePath, wc_path)
    if not Path.exists():
        print(f'wc: {wc_path}: No such file or directory')
        return
    if Path.is_dir():
        print(f'wc: {Path.name}: Is a directory')
        print(f'\t 0 \t 0 \t 0 {Path.name}')
        return f'\t {0} \t {0} \t {0}'
    try:
        len_bait = len(Path.read_bytes())
        with Path.open('r', encoding="utf8") as reader:
            text = reader.readlines()
        stroki = len(text)
        slova = 0
        for i in range(stroki):
            slova += len(text[i].split())
        print(f'\t {stroki} \t {slova} \t {len_bait} \t {Path.name}')
        return f'\t {stroki} \t {slova} \t {len_bait}'
    except UnicodeDecodeError:
        with zipfile.ZipFile(archivePath, 'a') as myzip:
            file_info = myzip.getinfo(wc_path)
            len_bait = file_info.file_size
            with myzip.open(wc_path) as img_file:
                img_data = img_file.read()
                stroki = img_data.count(b'\n')
                slova = len(img_data.split())
            print(f'\t {stroki} \t {slova} \t {len_bait} \t {Path.name}')


def main():
    vremen = {}
    config = configparser.ConfigParser()
    config.read('configuration.ini')
    name = config.get('User', 'name')
    archivePath = config.get('ArchivePath', 'value')
    startScriptPath = config.get('StartScriptPath', 'value')
    if not os.path.exists(archivePath) or not os.path.exists(startScriptPath):
        print("Error: Check ini файл!")
        return
    massiv = []
    with open(startScriptPath, 'r') as file:
        for line in file:
            massiv.append(line.strip())
    if zipfile.is_zipfile(archivePath):
        path_file = ''
        while True:
            if len(massiv):
                command = massiv[0]
                del massiv[0]
            elif len(path_file) == 0:
                command = input(f'{name + "@Configpc~" + path_file[:-1]}$ ').strip()
            else:
                command = input(f'{name + "@Configpc~/" + path_file[:-1]}$ ').strip()
            if command.startswith('exit'):
                break
            if command == 'ls':
                ls(archivePath, path_file)
            elif re.match(r'^ls\s+-l$', command):
                ls_l(archivePath, path_file, vremen)
            elif command.startswith('cd'):
                if command == 'cd':
                    path_file = ''
                elif re.match(r'^cd\s+\S+$', command):
                    path_file = cd(command.split(' ', 1)[1].lstrip(), path_file, archivePath)
                else:
                    print(f"bash: cd: too many arguments")
            elif command == 'touch':
                print('touch: missing file operand')
            elif command.startswith('touch '):
                touch(command.split(' ', 1)[1].lstrip(), path_file, archivePath, vremen)
            elif command == 'wc':
                print()
            elif command.startswith('wc '):
                wc(command.split(' ', 1)[1].lstrip(), path_file, archivePath)
            elif command:
                print(f'Unsupported command: {command}')


if __name__ == '__main__':
    main()