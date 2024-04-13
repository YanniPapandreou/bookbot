from typing import Dict, List

def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letter_counts = count_letters(text)
    print(f"{num_words} words found in the document\n")
    sorted_letter_counts = sort_letter_counts(letter_counts)
    for letter_dict in sorted_letter_counts:
        letter = letter_dict["letter"]
        count = letter_dict["count"]
        print(f"The '{letter}' character was found {count} times")


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_letters(text: str) -> Dict[str, int]:
    lowered_text = text.lower()
    counts = {}
    for letter in lowered_text:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    return counts

def sort_letter_counts(letter_counts: Dict[str, int]) -> List[Dict[str,str | int]]:
    list_of_dicts = [{"letter": k, "count": v} for k,v in letter_counts.items() if k.isalpha()]
    def sort_on(d: dict) -> int:
        return d["count"]

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts


main()
