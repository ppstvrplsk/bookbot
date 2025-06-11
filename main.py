def get_book_text(filepath):
    with open(filepath) as f:
    # do something with f (the file) here
        file_content = f.read()


def main():
    get_book_text("/home/kp/workspace/github.com/ppstvrplsk/bookbot/books/frankenstein.txt")



def count_words(filepath):
     with open(filepath) as f:
    # do something with f (the file) here
        file_content = f.read()
        words = file_content.split()
        num_words = words.count()
        print(num_words)
        
def main2():
    count_words("/home/kp/workspace/github.com/ppstvrplsk/bookbot/books/frankenstein.txt")
main2()
    