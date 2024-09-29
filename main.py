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
    with ZipFile('archive.rar', 'a') as file:
        path = '/'
        while True:
            command = input('$ ')
            if command == 'exit':
                break
            if command == 'ls':
                pass
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