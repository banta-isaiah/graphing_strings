def square(x):
    square = x * x
    return square


def file_to_string(file_name):
    text_file = open(file_name, 'r', encoding = 'utf-8')
    text_string = text_file.read().replace('\n', '')
    text_file.close()
    return text_string
    
    
def main():
    print(file_to_string('C:/Users/banta/coding/king_james.txt'))
main()