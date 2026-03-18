"""
Pin Extractor Project
---------------------

Concepts Practiced:
- Loops (for loops, iterating through sequences)
- Sequences (lists, strings)
- String manipulation (splitting strings, accessing words)
- Conditional statements (if-else)
- Functions and function arguments
"""

def pin_extractor(poems):
    """
    Extracts a 'secret code' from a list of poems.
    
    For each poem:
    - Takes the first line's first word, second line's second word, etc.
    - Calculates the length of each selected word
    - If the line has fewer words than its index, uses 0
    - Joins lengths together to form the secret code
    """
    secret_codes = []  # to store codes of all poems
    
    for poem in poems:  # process each poem one by one
        secret_code = ''
        lines = poem.split('\n')  # split poem into lines
        
        for line_index, line in enumerate(lines):
            words = line.split()  # split line into words
            
            # check if the line has enough words
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))  # add length of selected word
            else:
                secret_code += '0'  # use 0 if word is missing
        
        secret_codes.append(secret_code)  # add this poem's code to results
        
    return secret_codes

# Sample poems
poem1 = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"
poem3 = "There\nonce\nwas\na\ndragon"

# Call the function and print results
print(pin_extractor([poem1, poem2, poem3]))
