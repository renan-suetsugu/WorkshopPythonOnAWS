def open_input(file):
    with open(file, 'r') as file_text:
        text = file_text.read() #We use read() to read the actual contents of the file
        print(text)

def main():
    open_input("text.txt")

if __name__=="__main__":
    main()