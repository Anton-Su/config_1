from unittest import TestCase, main
import zip_program

config = zip_program.configparser.ConfigParser()
config.read('configuration.ini')
name = config.get('User', 'name')
archivePath = config.get('ArchivePath', 'value')
startScriptPath = config.get('StartScriptPath', 'value')


class Random(TestCase):
    def test_cd(self):
        self.assertEquals(zip_program.cd('/'))


if __name__ == '__main__':
    main()