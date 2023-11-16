from time import time


class Censored:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        text = []
        for world in value.split():
            if world.strip(',.!&?*/ ()').lower() == 'fuck':
                text.append(world.lower().replace('fuck', '****'))
            else:
                text.append(world)
        setattr(instance, self.name, ' '.join(text))


class Message:
    text = Censored()

    def __init__(self, text):
        self.text = text
        self.created_at = time()


class Song:
    name = Censored()
    author = Censored()

    def __init__(self, name, author):
        self.name = name
        self.auther = author
        self.created_at = time()


m1 = Message("Fuck, sofof.")
print(m1.text)

m2 = Message("Hello World!")
print(m2.text)
