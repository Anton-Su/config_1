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
    with ZipFile('archive.zip', 'a') as myzip:
        path = ''
        while True:
            command = input('$ ')
            if command == 'exit':
                break
            if command.startswith('ls'):
                for file in myzip.namelist():
                    if file.find(path) != -1 and file.count('/') + file.count('.') == path.count('/') + 1:
                        example = file
                        if (path):
                            example = file.split(path)[1]
                        print(example.strip('/'))
                        #print(file.replace('/', "").split('/'))
                    # if not file.find(path):
                    #     print(file)
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