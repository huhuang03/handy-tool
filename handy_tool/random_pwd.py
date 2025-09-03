import random
import string


def main():
    length = 10
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # 各类字符
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()-_=+[]{}<>?/"

    # 确保每类至少一个
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # 剩余长度随机选择
    all_chars = lower + upper + digits + special
    password += random.choices(all_chars, k=length-4)

    # 打乱顺序
    random.shuffle(password)

    return ''.join(password)