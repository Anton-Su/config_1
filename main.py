from zipfile import ZipFile
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
    with ZipFile(archivePath, 'a') as myzip:
        path = '\\'
        while True:
            command = input(f'{archivePath + path[:-1] }$ ').strip()
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
            elif command.startswith('cd '):
                _, path = command.split(' ', 1)


                pass
            elif command == 'touch':
                pass
            elif command == 'wc':
                pass
            else:
                print(f'Unsupported command: {command}')


if __name__ == '__main__':
    main()