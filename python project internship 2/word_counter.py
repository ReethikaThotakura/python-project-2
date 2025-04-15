# Enhanced Word Counter
# Counts words in text with a single input attempt
# Includes additional statistics for more functionality

def count_words(text):
    """
    Counts words in the given text and provides additional statistics.
    Returns a dictionary with word count, character count, and line count.
    """
    if not text.strip():
        return None
    
    lines = text.split('\n')
    words = text.split()
    characters = len(text.replace('\n', '').replace(' ', ''))
    
    return {
        'word_count': len(words),
        'character_count': characters,
        'line_count': len([line for line in lines if line.strip()]),
        'average_word_length': sum(len(word) for word in words) / len(words) if words else 0
    }

def display_results(stats):
    """
    Displays the counting results in a user-friendly format
    """
    print("\n=== Text Analysis Results ===")
    print(f"Word count: {stats['word_count']}")
    print(f"Character count (excluding spaces): {stats['character_count']}")
    print(f"Line count: {stats['line_count']}")
    print(f"Average word length: {stats['average_word_length']:.1f} characters")

def get_user_text():
    """
    Gets user input in a single attempt with clear instructions
    """
    print("""=== Enhanced Word Counter ===
Enter your text below (press Enter when finished):
--------------------------------------------------""")
    return input()

def main():
    """
    Main program flow
    """
    user_text = get_user_text()
    
    if not user_text.strip():
        print("\nError: No text entered! Please try again.")
        return
    
    stats = count_words(user_text)
    
    if stats:
        display_results(stats)
    else:
        print("\nError: No valid words found in the input.")

if __name__ == "__main__":
    main()