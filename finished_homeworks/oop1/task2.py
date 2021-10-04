# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.

class Person:
    """
    Make the class with composition.
    """

    def __init__(self):
        arm = Arm("Humans arm")


class Arm:
    """
    Make the class with composition.
    """

    def __init__(self, info_about_arm):
        self.info_about_arm = info_about_arm
        print(self.info_about_arm)


human = Person()


class CellPhone:
    """
    Make the class with aggregation
    """

    def __init__(self, screen_phone):
        self.screen_phone = screen_phone


class Screen:
    """
    Make the class with aggregation
    """

    def __init__(self):
        pass


screen_phone_ = Screen()
cell_phone = CellPhone(screen_phone_)
