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
    with ZipFile('archive.zip', 'a') as archiv:
        path = 'archive.7z'
        while True:
            command = input('$ ')
            if command == 'exit':
                break
            if command.startswith('ls'):
                print(archiv.namelist())
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