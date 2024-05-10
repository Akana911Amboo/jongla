class dog:
    def __init__ (self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

a = dog("Dawa", "golden", 7)
b = dog("Nima","red", 4)
c = dog("Blacky", "napp", 9)

print(a.color, a.age, a.name)
print(b.age, b.name, b.color)
print(c.age, c.name, c.color)

