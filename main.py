import zipfile
import configparser
import os
import io


def ls(archivePath, path_file):
    Path = zipfile.Path(archivePath, path_file[1:])
    for i in Path.iterdir():
        print(i.name)


def cd(command, path_file, archivePath):
    command_and_path = command.split(' ', 1)
    if len(command_and_path) == 1:
        path_file = '/'
        return path_file
    maybe_path = command_and_path[1]
    if not maybe_path.startswith('/'):  # не по абсолютному пути
        maybe_path = path_file[1:] + maybe_path
    Path = zipfile.Path(archivePath, maybe_path)
    if Path.is_file() and Path.exists():
        print(f"bash: cd: {Path.name}: Not a directory")
        return path_file
    if not maybe_path.endswith('/'):
        Path = zipfile.Path(archivePath, maybe_path + '/')
    if Path.is_dir() and Path.exists():
        path_file = '/' + Path.name + '/'
        return path_file
    print(f"bash: cd: {maybe_path}: No such file or directory")
    return path_file


def touch(command, path_file, archivePath):
    with zipfile.ZipFile(archivePath, 'a') as myzip:
        touch = command.split(" ", 1)
        if len(touch) > 1:
            Path = zipfile.Path(archivePath, path_file[1:] + touch[1])
            if not Path.exists():
                path_to_file = path_file[1:] + touch[1]
                myzip.writestr(path_to_file, "")


def wc(command, path_file, archivePath):
    wc = command.split(" ", 1)
    if len(wc) > 1:
        Path = zipfile.Path(archivePath, path_file[1:] + wc[1])
        if Path.exists() or zipfile.Path(archivePath, path_file[1:] + wc[1] + '/'):
            if Path.is_file():
                len_bait = len(Path.read_bytes())
                with Path.open('r') as reader:
                    text = reader.readlines()
                stroki = len(text)
                slova = 0
                for i in range(stroki):
                    slova += len(text[i].split())
                print(f'\t {stroki} \t {slova} \t {len_bait}')
            else:
                print(f'wc: {Path.name}: Is a directory')
                print(f'\t 0 \t 0 \t 0 {Path.name}')


def main():
    config = configparser.ConfigParser()
    config.read('configuration.ini')
    name = config.get('User', 'name')
    archivePath = config.get('ArchivePath', 'value')
    startScriptPath = config.get('StartScriptPath', 'value')
    if not os.path.exists(archivePath) or not os.path.exists(startScriptPath):
        print("Error: Check ini файл!")
        return
    os.system(startScriptPath)
    print(f"Вводите команды, {name}!")
    if zipfile.is_zipfile(archivePath):
        with zipfile.ZipFile(archivePath, 'a') as myzip:
            path_file = '/'
            while True:
                command = input(f'{archivePath + path_file[:-1]} $ ').strip()
                if command == 'exit':
                    break
                if command == 'ls':
                    ls(archivePath, path_file)
                elif command.startswith('cd'):
                    path_file = cd(command, path_file, archivePath)
                elif command.startswith('touch'):
                    touch(command, path_file, archivePath)
                elif command.startswith('wc'):
                    wc(command, path_file, archivePath)
                else:
                    print(f'Unsupported command: {command}')


if __name__ == '__main__':
    main()