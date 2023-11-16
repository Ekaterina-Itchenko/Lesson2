class Contact:
    def __init__(self, email, phone, first_name, last_name):
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if len(value.split('@')) != 2:
            raise ValueError('An Email must contains only one "@".')
        elif value.split('@')[1] not in ('gmail.com', 'yandex.ru',
                                         'ya.ru', 'yahoo.com'):
            raise ValueError('Unsupported email provider.')
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not value.startswith('+'):
            raise ValueError('A phone number must starts with +.')
        if not value[1:].startswith(('375', '48', '374')):
            raise ValueError('Incorrect country code.')
        self._phone = value

    def _validate_name(self, name):
        if not name[0].isupper():
            raise ValueError('The Name must starts with capital letter.')
        if len(name) not in range(5, 16):
            raise ValueError('A phone number length must'
                             ' be in range(5, 15).')

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._validate_name(value)
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._validate_name(value)
        self._last_name = value


person_1 = Contact('katerina@gmail.com',
                   '+48295664578',
                   'Katerina',
                   'Itchenko')
print(person_1.first_name)
