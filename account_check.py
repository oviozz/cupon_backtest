
from nagivation import ScreenNavigate

class SignUp:
    def __init__(self):
        self.accounts = open("signup_log", 'a')

    def create_account(self, username, password, screen):
        if username and password:
            self.accounts.write(f'{username}:{password}\n')
            ScreenNavigate.screen_change(screen, 1)


class Login(SignUp):

    def read_account(self,username, password, screen):
        self.accounts = open("signup_log", 'r')
        accounts = {i.split(':')[0]:i.split(':')[1].replace('\n','') for i in [i for i in self.accounts.readlines()] if i}
        self.accounts.close()
        print(accounts)
        return ScreenNavigate.screen_change(screen, 2) if accounts.get(username.text()) == password.text() else username.setText(''),password.setText('')


