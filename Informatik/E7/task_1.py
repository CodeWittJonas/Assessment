class Password:

    def __init__(self, name, username, password):
        self.__name = name
        self.__username = username
        self.__password = password

    def __str__(self):
        masked_password = ""
        for char in self.__password:
            masked_password = masked_password + "*"

        return "{}: {} / {}".format(self.__name, self.__username, masked_password)

    def pretty_str_password(self):
        return "{}: {} / {}".format(self.__name, self.__username, self.__password)


class PasswordManager:

    def __init__(self, master_password):
        self.__master_password = master_password
        self.__passwords = {}
        self.unlocked = False

    def lock(self):
        self.unlocked = False

    def unlock(self, master_password):
        if master_password == self.__master_password:
            self.unlocked = True
            return True
        else:
            return False

    def create_new_password(self, name, username, password):
        if not self.unlocked:
            return None

        if name in self.__passwords:
            return None

        else:
            new_credentials = Password(name, username, password)
            self.__passwords[name] = new_credentials
            return new_credentials

    def update_password(self, name, username, password):
        if not self.unlocked:
            return None

        if name in self.__passwords:
            new_credentials = Password(name, username, password)
            self.__passwords[name] = new_credentials
            return new_credentials

        else:
            return None

    def get_password(self, name):
        if not self.unlocked:
            return None

        if name in self.__passwords:
            return self.__passwords[name]

        else:
            return None

    def list_passwords(self):
        password_list = []
        if self.unlocked:
            for password in self.__passwords:
                password_list.append(self.__passwords[password].pretty_str_password())
            return password_list

        else:
            for password in self.__passwords:
                password_list.append(self.__passwords[password].__str__())
            return password_list


