from errors import ChoiceError


def validate_user_choice(user_choice: str) -> None:
    if not user_choice.isdigit():
        raise ChoiceError("Choice must be digit.")

    if user_choice not in ("1", "2"):
        raise ChoiceError("Choice must be 1 or 2.")
