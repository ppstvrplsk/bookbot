def get_book_text(filepath):
    with open(filepath) as f:
    # do something with f (the file) here
        file_content = f.read()

def count_words(filepath):
     with open(filepath) as f:
    # do something with f (the file) here
        print (f"{(len(f.read().split()))} words found in the document")

def count_letters(filepath):
    with open(filepath) as f:
        file_content = f.read()
        counter = {}
        for i in file_content:
            x = i.lower()
            if x in counter:
                counter[x] += 1
            else:
                counter[x] = 1
        print (counter)
                

