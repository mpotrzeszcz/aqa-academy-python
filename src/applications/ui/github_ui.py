from src.applications.ui.pages.login_page import LoginPage


class GitHubUI:

    def __init__(self) -> None:
        self.login_page = LoginPage()

    def try_login(username: str, password: str):
        self.login_page.login()

    def logout(self):
        pass

    def create_user(self):
        pass
