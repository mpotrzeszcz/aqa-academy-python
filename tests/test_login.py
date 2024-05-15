def test_negative_login(GitHubUI):
    """
    Summary: Test negative login attempt

    Steps:
    1. Navigate to login page
    2. Enter wrong login credentials
    3. Click login button

    Expected result:
    Error saying "Incorrect username or password." appears.
    """

    GitHubUI.open()
    GitHubUI.login_page.navigate_to()

    GitHubUI.try_login(username="najfjasbjk", password="najfjasbjk")

    # username_fld = GitHubUI.login_page.find_username_fld()
    # username_fld.enter_text("najfjasbjk")

    # password_fld = GitHubUI.login_page.find_password_fld()
    # password_fld.enter_text("najfjasbjk")

    # singin_btn = GitHubUI.login_page.find_singin_btn()
    # singin_btn.click()

    assert GitHubUI.login_psgr.check_wrong_cred_message()

    # error_message = GitHubUI.login_page.find_error_message()
    # assert error_message.text() == "Incorrect username or password."

    GitHubUI.close()
