def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    book_len = get_book_length(text)
    print(f"{book_len} words found in the text!")
    chars_dict = count_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{book_len} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_length(text):
    split_text = text.split()
    return len(split_text)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def count_letters(text):
    chars = {}
    for letter in text:
        lower = letter.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
