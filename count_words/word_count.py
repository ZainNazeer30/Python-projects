def words_count_file(filename):
    try:
        
        with open(filename,'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"The total number of words in that file '{filename}': is {word_count}")
    except FileNotFoundError:
        print(f"Error! the '{filename}' not found.")
    
file_name = input("Enter file name to count words: ")
words_count_file(file_name)
        
        