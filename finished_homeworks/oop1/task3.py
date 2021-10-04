# 3.


class Profile:
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    """

    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"name: {self.name}"


my_profile = Profile('Bohdan', 'last_name', 'phone_number', 'address', 'email', 'birthday', 'age', 'sex111')
print(my_profile)

# import inspect
#
# signature1 = inspect.signature(Profile.__init__)
# a = []
# for param in signature1.parameters.values():
#     a.append(param.name)
# print(a)
