import re
from collections import Counter
from typing import Optional

 #c4fcbee0ebc6cb56b1dca96ce70fadbb
def split_words(text: str) -> list[str]:
    return re.findall(r"[a-zA-Zа-яА-ЯёЁ0-9]+", text.lower())


def count_word_frequencies(words: list[str]) -> dict[str, int]:
    return dict(Counter(words))


def top_word(freq: dict[str, int]) -> Optional[str]:
    return max(freq, key=freq.get) if freq else None


if __name__ == "__main__":
    TEXT = (
        "Я достаю из широких штанин дубликатом бесценного груза. "
        "Читайте, завидуйте, я — гражданин Советского Союза."
    )

    print("1) split_words:")
    print(split_words(TEXT))
    print()

    print("2) count_word_frequencies:")
    print(count_word_frequencies(split_words(TEXT)))
    print()

    print("3) top_word:")
    print(top_word(count_word_frequencies(split_words(TEXT))))
    print()

    print("4) пустая строка:")
    print(top_word({}))
