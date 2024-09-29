from zipfile import ZipFile


def ls(path):
    pass


def cd(path):
    pass


def touch(path):
    pass


def wc(path):
    pass


def main():
    with ZipFile('archive.7z', 'a') as file:
        path = '/'
        while True:
            command = input('$ ')
            if command == 'exit':
                break
            if command.startswith('ls'):
                for fil in file.namelist():
                    print(fil)
            elif command == 'cd':
                pass
            elif command == 'touch':
                pass
            elif command == 'wc':
                pass
            else:
                print(f'Unsupported command: {command}')


if __name__ == '__main__':
    main()