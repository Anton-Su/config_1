import zipfile
import configparser
import os


def ls(path):
    pass


def cd(path):
    pass


def touch(path):
    pass


def wc(path):
    pass


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
                if command.startswith('ls'):
                    Path = zipfile.Path(archivePath, path_file[1:])
                    for i in Path.iterdir():
                        print(''.join(str(i).split('.zip/', 1)[1]).strip('/'))

                elif command.startswith('cd'):
                    command_and_path = command.split(' ', 1)
                    if len(command_and_path) == 1:
                        path_file = '/'
                        continue
                    maybe_path = command_and_path[1]
                    if not maybe_path.startswith('/'):  # не по абсолютному пути
                        maybe_path = path_file[1:] + maybe_path
                    Path = zipfile.Path(archivePath, maybe_path)
                    if Path.is_file() and Path.exists():
                        path_file = '/' + ''.join(str(Path).split('.zip/', 1)[1])
                        continue
                    if not maybe_path.endswith('/'):
                        Path = zipfile.Path(archivePath, maybe_path + '/')
                    if Path.is_dir() and Path.exists():
                        path_file = '/' + ''.join(str(Path).split('.zip/', 1)[1])
                        continue
                    print(f"bash: cd: {maybe_path}: No such file or directory")
                elif command == 'touch':
                    pass
                elif command == 'wc':
                    pass
                else:
                    print(f'Unsupported command: {command}')


if __name__ == '__main__':
    main()