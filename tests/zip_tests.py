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

    def test_ls_1(self):
        self.assertEqual(zip_program.ls(archivePath, ''), ['empty folder', 'folder_1', 'folder_2', 'folder_3', 'folder_4', 'folder_5', 'originally folder', 'hm.txt', 'h', 'privet.txt'])

    def test_ls_2(self):
        self.assertEqual(zip_program.ls(archivePath, '/folder_1/1/hey-hey/'), ['totally normal_photo_1.jpg', 'totally normal_photo_2.jpg'])

    def test_ls_3(self):
        self.assertEqual(zip_program.ls(archivePath, '/originally folder/'), ['folder 2-2', 'surprize!'])



if __name__ == '__main__':
    main()