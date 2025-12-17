from typing import TypedDict


class CharNum(TypedDict):
    char: str
    num: int


def get_book_text(path: str):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def count_words(content: str):
    words_list = content.split()
    num_words = len(words_list)
    print(f"Found {num_words} total words")


def count_chars(content: str) -> dict[str, int]:
    normalised_content = content.lower()
    res: dict[str, int] = {}
    for char in normalised_content:
        if not char.isalpha():
            continue
        if char not in res:
            res[char] = 1
        else:
            res[char] += 1

    return res


def chars_to_list(dict: dict[str, int]):
    res: list[CharNum] = []
    for key, value in dict.items():
        res.append({"char": key, "num": value})
    res.sort(key=lambda x: x["num"], reverse=True)

    for r in res:
        print(f"{r['char']}: {r['num']}")
