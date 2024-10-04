from unittest import TestCase, main
import zip_program

config = zip_program.configparser.ConfigParser()
config.read(r'C:\Users\Antua\PycharmProjects\config1\configuration.ini')
name = config.get('User', 'name')
archivePath = config.get('ArchivePath', 'value')
startScriptPath = config.get('StartScriptPath', 'value')


class Random(TestCase):
    def test_cd_1(self):
        self.assertEqual(zip_program.cd(['cd', '123'], '/', archivePath), '/')

    def test_cd_2(self):
        self.assertEqual(zip_program.cd(['cd', 'folder_1'], '/', archivePath), '/folder_1/')

    def test_cd_3(self):
        self.assertEqual(zip_program.cd(['cd', 'folder_1/2'], '/', archivePath), '/2/')

    def test_cd_4(self):
        self.assertEqual(zip_program.cd(['cd', ''], '/', archivePath), '/')

if __name__ == '__main__':
    main()