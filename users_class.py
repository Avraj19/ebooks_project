from people_class import People

class User(People):

    def __init__(self, name,  phone_num, email, user_type='Staff'):
        super().__init__(name, phone_num, email)
        self.name = name.title()
        self.phone_num = phone_num
        self.email = email.strip()
        self.user_type = user_type
