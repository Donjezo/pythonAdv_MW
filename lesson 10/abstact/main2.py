from abc import abstractclassmethod


class Animal:
    @abstractclassmethod
    def make_soud(self):
        pass


class Dog(Animal):
    def make_soud(self):
        print("ham ham ")


dog1=Dog()
dog1.make_soud()