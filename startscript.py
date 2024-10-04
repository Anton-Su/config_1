import main

config = main.configparser.ConfigParser()
config.read('configuration.ini')
name = config.get('User', 'name')
archivePath = config.get('ArchivePath', 'value')
startScriptPath = config.get('StartScriptPath', 'value')


def fun():
    main.ls(archivePath, '/')
    main.touch('touch privet.txt', '/', archivePath)
    main.wc('wc privet.txt', '/', archivePath)


if __name__ == '__main__':
    fun()