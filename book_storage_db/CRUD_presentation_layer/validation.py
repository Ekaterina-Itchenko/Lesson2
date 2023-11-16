from CRUD_presentation_layer.exeptions import InvalidChoice, NotDigitError


def validate_choice(choice: str, start: int, stop: int):
    if not choice.isdigit():
        raise InvalidChoice('Your choice must be an integer.')
    if int(choice) not in range(start, stop + 1):
        raise InvalidChoice('Invalid number of choice.')


def validate_id(id_number):
    if not id_number.isdigit() or not id_number:
        raise NotDigitError('An id must be an integer.')
