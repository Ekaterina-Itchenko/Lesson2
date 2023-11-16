from errors import NotDigitError, UnexpectedNumberError, DigitError


def validator_choice(choice: str) -> None:
    if not choice.isdigit():
        raise NotDigitError('Your choice must be a digit.')
    elif int(choice) not in range(1, 8):
        raise UnexpectedNumberError('Enter a digit from 1 to 7')


def check_id(product_id: str) -> None:
    if not product_id.isdigit():
        raise NotDigitError('Product id must be a digit.')


def check_amount(amount: str) -> None:
    if int(amount) < 0:
        raise DigitError("Amount of goods must be positive.")
    if not amount.isdigit():
        raise NotDigitError('Amount of goods must be a digit.')
