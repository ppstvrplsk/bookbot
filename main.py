def get_book_text(filepath):
    with open(filepath) as f:
    # do something with f (the file) here
        file_content = f.read()

def count_words(filepath):
     with open(filepath) as f:
    # do something with f (the file) here
        print (f"{(len(f.read().split()))} words found in the document")
     
def main():
    count_words("/home/kp/workspace/github.com/ppstvrplsk/bookbot/books/frankenstein.txt")

main()



   
        

    