from unittest import TestCase, main
import zip_program

config = zip_program.configparser.ConfigParser()
config.read(r'C:\Users\Antua\PycharmProjects\config1\configuration.ini')
name = config.get('User', 'name')
archivePath = config.get('ArchivePath', 'value')
startScriptPath = config.get('StartScriptPath', 'value')


class Random(TestCase):
    def test_cd(self):
        self.assertEqual(zip_program.cd(['cd', '123'], '/', archivePath), '/')


# if __name__ == '__main__':
#     main()