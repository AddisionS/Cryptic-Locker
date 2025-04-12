import os

class SignUp():
    def __init__(self):
        super().__init__()

    def username_check(self, name):
        vault_path = "../vault"
        username_file = f"{name}.acrl"

        if not os.path.exists(vault_path):
            os.makedirs(vault_path)

        return not os.path.exists(os.path.join(vault_path, username_file))