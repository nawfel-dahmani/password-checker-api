import random
import string
import re
from models import PasswordResponse

def check_password(password: str) -> PasswordResponse:
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("12+ characters makes it much stronger.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters like !@#$%.")

    strength_map = {
        0: "Very Weak", 1: "Weak", 2: "Fair",
        3: "Fair", 4: "Strong", 5: "Very Strong"
    }

    return PasswordResponse(
        password=password,
        score=score,
        strength=strength_map[score],
        feedback=feedback,
        is_strong=score >= 4
    )


def generate_strong_password(length: int = 16) -> str:
    characters = (
            string.ascii_uppercase +
            string.ascii_lowercase +
            string.digits +
            "!@#$%^&*()"
    )
    # Guarantee at least one of each required type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()")
    ]
    # Fill the rest randomly
    password += random.choices(characters, k=length - 4)

    # Shuffle so the guaranteed chars aren't always at the start
    random.shuffle(password)
    return "".join(password)