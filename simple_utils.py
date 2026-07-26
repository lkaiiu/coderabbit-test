# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Reverse the characters in text.
    
    Parameters:
        text: The string to reverse.
    
    Returns:
        The reversed string.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the whitespace-separated words in a sentence.
    
    Parameters:
    	sentence (str): The text whose words are counted.
    
    Returns:
    	int: The number of whitespace-separated words.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.
    
    Parameters:
    	celsius (float): The temperature in degrees Celsius.
    
    Returns:
    	float: The equivalent temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32
