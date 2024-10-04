import zip_program

config = zip_program.configparser.ConfigParser()
config.read('configuration.ini')
name = config.get('User', 'name')
archivePath = config.get('ArchivePath', 'value')
startScriptPath = config.get('StartScriptPath', 'value')


def fun():
    zip_program.ls(archivePath, '/')
    zip_program.touch('touch privet.txt', '/', archivePath)
    zip_program.wc(['wc', 'privet.txt'], '/', archivePath)


if __name__ == '__main__':
    fun()