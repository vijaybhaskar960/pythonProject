import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\vijay\PycharmProjects\pythonProject2\POM\Configurations\config.ini")


class ReadConfig():

    @staticmethod
    def getApllicationURL():
       url = config.get('common info', 'baseURL')
       return url



    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

