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
                    pass
                # path_1 = path
                # flag = False
                # if len(command.split()) == 2:
                #     path_1 = command.split()[1]
                # for file in myzip.namelist():
                #     if file.find(path_1) != -1:
                #         flag = True
                #         if file.count('/') + file.count('.') == path_1.count('/') + 1:
                #             example = file
                #             if (path_1):
                #                 example = file.split(path_1)[1]
                #             print(example.strip('/'))
                elif command.startswith('cd'):
                    command_and_path = command.split(' ', 1)
                    maybe_path = '/'
                    if len(command_and_path) != 1:
                        maybe_path = command_and_path[1]
                    if not maybe_path.startswith('/'):  # не по абсолютному пути
                        maybe_path = path_file + maybe_path
                    Path = zipfile.Path(archivePath, maybe_path)
                    # for i in Path.iterdir():
                    #     print(str(i).split('.zip/', 1))
                    # print(list(Path.iterdir()))
                    if Path.is_file():
                        path_file = ''.join(str(Path).split('.zip/', 1))
                        continue
                    if not maybe_path.endswith('/'):
                        Path = zipfile.Path(archivePath, maybe_path + '/')
                    if Path.is_dir():
                        path_file = ''.join(str(Path).split('.zip/', 1))
                        continue
                    print(f"bash: cd: {maybe_path}: No such file or directory")
                    # for i in Path.iterdir():
                    #     print(i)
                    # print(list(Path.iterdir()))
                    # pass
                elif command == 'touch':
                    pass
                elif command == 'wc':
                    pass
                else:
                    print(f'Unsupported command: {command}')


if __name__ == '__main__':
    main()