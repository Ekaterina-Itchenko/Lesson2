from errors import NotDigitError, UnexpectedNumberError


def check_choice(choice: str) -> None:
    if not choice.isdigit():
        raise NotDigitError('Your choice must be a digit.')
    elif int(choice) not in range(1, 11):
        raise UnexpectedNumberError('Enter a digit from 1 to 5')
