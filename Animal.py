class Animal:
    def make_sound(self, sound="Some animal sound"):
        print(sound)
    def move(self):
        return "moves"
        
class Dog(Animal):
    def make_sound(self):
        super().make_sound("Woof")
    def move(self):
        return "runs"
    
class Cat(Animal):
    def make_sound(self):
        super().make_sound("Meow")
    def move(self):
        return "walk silent"
    
class Cow(Animal):
    def make_sound(self):
        super().make_sound("Moo")
    def move(self):
        return "walk slowly"
        
Dog().make_sound()

