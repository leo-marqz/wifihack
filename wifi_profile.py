
class WifiProfile:
    def __init__(self, name:str, password:str):
        self.name = name
        self.password = password

    def __str__(self):
        return f'Wifi Profile => Name: {self.name} | Password: {self.password}'    
