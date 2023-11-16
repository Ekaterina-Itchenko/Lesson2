from providers import PhoneProvider
from errors import ValidationError


class Validator:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValidationError(f"{self.name} must be more than 0.")
        setattr(instance, self.name, value)


class FakeFactory:
    number_of_records = Validator()

    def __init__(self, provider, number_of_records):
        self.provider = provider
        self.number_of_records = number_of_records

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.number_of_records:
            self.counter += 1
            return self.generate()
        else:
            raise StopIteration

    def generate(self):
        return self.provider()


fake = FakeFactory(PhoneProvider(), 2)
print(fake.generate())
print()

for email in fake:
    print(email)
