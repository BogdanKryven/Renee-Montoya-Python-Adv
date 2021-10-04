# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
from abc import ABC, abstractmethod


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def web_cam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def screen(self):
        print("Screen for HP Laptop")

    def keyboard(self):
        print("Keyboard for HP Laptop")

    def touchpad(self):
        print("Touchpad for HP Laptop")

    def web_cam(self):
        print("WebCam for HP Laptop")

    def ports(self):
        print("Ports for HP Laptop")

    def dynamics(self):
        print("Dynamics for HP Laptop")


HP = HPLaptop()
HP.web_cam()


# class HPLaptop(Laptop):
#     model = {}
#     # def __init__(self):
#     #     self.model = {}
#
#     def screen(self):
#         self.model['screen'] = 'LCD'
#
#     def keyboard(self):
#         self.model['keyboard'] = 'logitech'
#
#     def touchpad(self):
#         self.model['touchpad'] = 'HP'
#
#     def webcam(self):
#         self.model['webcam'] = 'logitech'
#
#     def ports(self):
#         self.model['ports'] = 'usb'
#
#     def dynamics(self):
#         self.model['dynamic'] = 'HP'
#
#     def __str__(self):
#         return f'{self.model}'
#
#
# HP_laptop = HPLaptop()
# HP_laptop.screen()
# HP_laptop.webcam()
# HP_laptop.dynamics()
# HP_laptop.ports()
# print(HP_laptop)
