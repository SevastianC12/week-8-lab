# Write a program that gets a string containing a person’s first, middle, and last names, and displays their first, middle, and last initials.

def get_initials(full_name):
    # Split the full name into parts
    name_parts = full_name.split()
    
    # Extract the first, middle, and last initials
    initials = [part[0].upper() + '.' for part in name_parts]
    
    
    return ' '.join(initials)

# Get user input
full_name = input("Enter your first, middle, and last names: ")

# Display 
print(get_initials(full_name))


#Write a program that asks the user to enter a series of single-digit numbers with nothing separating them.

def sum_of_digits(number_string):
    # Initialize the sum
    total_sum = 0
    
    # Loop through each character in the string
    for char in number_string:
        # Convert the character to an integer and add it to the sum
        total_sum += int(char)
    
    return total_sum

# Get user input
user_input = input("Enter a series of single-digit numbers (e.g., 2514): ")

# Calculate and display
result = sum_of_digits(user_input)
print("The sum of the digits is:", result)


#Write a program that reads a string from the user containing a date in the form mm/dd/yyyy.

from datetime import datetime

# Function to convert date format
def convert_date(date_str):
    # Parse the input date string
    date_obj = datetime.strptime(date_str, '%m/%d/%Y')
    # Format the date in the desired output format
    return date_obj.strftime('%B %d, %Y')

# Main program
if __name__ == "__main__":
    # Read date from user
    date_input = input("Enter a date (mm/dd/yyyy): ")
    try:
        # Convert and print the formatted date
        formatted_date = convert_date(date_input)
        print("Formatted date:", formatted_date)
    except ValueError:
        print("Invalid date format. Please enter the date in mm/dd/yyyy format.")




#Write a program that asks the user to enter a string, then converts that string to Morse code.

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += '? '  
    return morse_code.strip()

# Ask user for input
user_input = input("Enter a string to convert to Morse code: ")
morse_output = text_to_morse(user_input)

print("Morse code:", morse_output)





#Write a program that askj the user to enter 10 digit phone number and then display the telephone number with any alphabetic characters.
# Mapping of letters to digits
letter_to_digit = {
    'A': '2', 'B': '2', 'C': '2',
    'D': '3', 'E': '3', 'F': '3',
    'G': '4', 'H': '4', 'I': '4',
    'J': '5', 'K': '5', 'L': '5',
    'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7',
    'T': '8', 'U': '8', 'V': '8',
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
}

def convert_to_numeric(phone_number):
    numeric_number = ''
    for char in phone_number:
        if char.isalpha():
            numeric_number += letter_to_digit[char.upper()]
        else:
            numeric_number += char
    return numeric_number

# Main program
def main():
    user_input = input("Enter a 10-character telephone number in the format XXX-XXX-XXXX: ")

    # Validate input length and format
    if len(user_input) != 14 or user_input[3] != '-' or user_input[7] != '-':
        print("Invalid format. Please enter the number in the format XXX-XXX-XXXX.")
        return

    # Convert to numeric format
    numeric_output = convert_to_numeric(user_input)
    print("Numeric telephone number:", numeric_output)

# Run the program
if __name__ == "__main__":
    main()



#Write a program that reads the file’s contents and calculates the average number of words per sentence.
def average_words_per_sentence(file_path):
    try:
        with open(file_path, 'r') as file:
            sentences = file.readlines()
        
        total_sentences = len(sentences)
        total_words = 0

        for sentence in sentences:
            words = sentence.split()
            total_words += len(words)

        if total_sentences > 0:
            average = total_words / total_sentences
        else:
            average = 0

        return average

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
file_path = 'text.txt'
average = average_words_per_sentence(file_path)
if average is not None:
    print(f"The average number of words per sentence is: {average:.2f}")


#Write a program that reads the file's contents and determines the following: The number of uppercase letters, The number of lowercase, and the number of digits.
def count_characters(file_path):
    # Initialize counters
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    whitespace_count = 0

    # Open the file and read its contents
    with open(file_path, 'r') as file:
        contents = file.read()

        # Iterate through each character in the contents
        for char in contents:
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1
            elif char.isdigit():
                digit_count += 1
            elif char.isspace():
                whitespace_count += 1

    # Print the results
    print(f"Uppercase letters: {uppercase_count}")
    print(f"Lowercase letters: {lowercase_count}")
    print(f"Digits: {digit_count}")
    print(f"Whitespace characters: {whitespace_count}")

# Replace 'text.txt' with the path to your file
count_characters('text.txt')



#Write a program with a function that accepts a string as an argument and returns a copy of the string with the first characters of each sentence capitalized.

def capitalize_words(text):
    # Split the text into sentences using '. ' as the delimiter
    sentences = text.split('. ')
    # Capitalize the first letter of each word in each sentence
    capitalized_sentences = [' '.join(word.capitalize() for word in sentence.split()) for sentence in sentences]
    # Join the sentences back with '. ' and return the result
    return '. '.join(capitalized_sentences)

# Prompt the user for input
user_input = input("Please enter a sentence: ")
output_text = capitalize_words(user_input)
print(output_text)



# Main function 
def main():
    # Get a string from the user.
    user_str = input('Enter a string of characters: ')
    # Report the vowels and consonants. 
    print('That string has', num_vowels(user_str), 'vowels and', num_consonants(user_str), 'consonants.')

# The num_vowels function returns the number of
# vowels in the string passed as an argument.
def num_vowels(s):
    # Make a list containing the vowels.
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Initialize an accumulator 
    v_count = 0
    # Count the vowels in s.
    for ch in s:  # Changed from ';' to ':'
        if ch.lower() in vowels:
            v_count += 1
    # Return the vowel count. 
    return v_count

# The num_consonants function returns the number of 
# consonants in the string passed as an argument.
def num_consonants(s):
    # Make a list containing the vowels.
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Initialize an accumulator.
    c_count = 0
    # Count the consonants in s.
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1 
    # Return the consonant count.
    return c_count
# Call the main function. 
main()



#Write a program that lets the user to enter a string and displays the character that appears most frequently in the string.
def most_frequent_char(s):
    # Create a dictionary to count the frequency of each character
    frequency = {}
    
    for char in s:
        if char.isalpha():  # Count only alphabetic characters
            frequency[char] = frequency.get(char, 0) + 1
    
    # Find the character with the highest frequency
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent, frequency[most_frequent]

# Main function
def main():
    # Get a string from the user
    user_str = input("Enter a string: ")
    char, count = most_frequent_char(user_str)
    print(f"The character that appears most frequently is '{char}' with {count} occurrences.")

# Call the main function
if __name__ == "__main__":
    main()
