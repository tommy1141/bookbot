def get_book_text(input_file):
    with open(input_file) as b:
        book_contents = b.read()
        return book_contents
    
def word_count(content):
    split = content.split()
    num_words = len(split)
    return num_words

def sort_on(items):
    return items['num']

def sorted_list(dic):
    list = []
    for letter,count in dic.items():
        list.append({'char':letter, 'num':count})
    return sorted(list,reverse=True,key=sort_on)

def times_used(content):
    letters = {}
    split = content.split()
    for i in split:
        a = i.lower()
        for b in a:
            if b not in letters:
                letters[b] = 0
            letters[b] += 1
    return sorted_list(letters)


def report(filename):
    content = get_book_text(filename)
    num_words = word_count(content)
    num_char = times_used(content)
    report = f"============ BOOKBOT ============\n"
    report += f"Analyzing book found at {filename} \n"
    report += f"----------- Word Count ----------\n"
    report += f"Found {num_words} total words\n"
    report += f"--------- Character Count -------\n"
    for item in num_char:
        if item['char'].isalpha():  # Only include alphabetic characters
            report += f"{item['char']}: {item['num']}\n"

    report += f"============= END ===============\n"
    return report