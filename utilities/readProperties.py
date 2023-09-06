import configparser

config = configparser.RawConfigParser()
config.read("D:\Framework\Configurations\config.ini")

class ReadConfig():
    
    @staticmethod
    def get_base_url():
        base_url = config.get('common info','base_url')
        return base_url

    @staticmethod
    def get_username():
        username = config.get('common info','username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info','password')
        return password
