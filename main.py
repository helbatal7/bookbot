def fran_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
    
def get_char_count(text):
    txt = text.lower()
    char_count = {}
    for char in txt:
        if char.isalpha():
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return char_count

def sort_on(dict):
    return dict["num"]

def main():
    text = fran_text()
    char_count = get_char_count(text)
    char_count = [{"char": k, "num": v} for k, v in char_count.items()]
    char_count.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Total characters: {len(text.split())}\n")
    for i in char_count:
        print(f"Character count for '{i['char']}': {i['num']}")
    print("--- End report ---")

if __name__ == '__main__':
    main()