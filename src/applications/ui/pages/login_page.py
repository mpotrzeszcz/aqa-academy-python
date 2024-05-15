class LoginPage:

    URL = "https://github.com/login"
    LOGIN_FLD = '//*[@id="login_field"]'
    PASSWORD_FLD = '//*[@id="password"]'
    SIGNIN_BTN = '//*[@id="login"]/div[4]/form/div/input[13]'

    def try_login(self, username: str, password: str):
        pass

    def check_wrong_creds_message(self):
        pass
        # return False/True
