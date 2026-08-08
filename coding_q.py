
CODING_PROBLEMS = [
    {
        "title": "Anagram Check",
        "description": (
            "Read two strings (one per line). Print 'Yes' if they are "
            "anagrams of each other (same letters, same counts, ignoring "
            "case), otherwise print 'No'.\n\n"
            "Example:\n"
            "Input:\nlisten\nsilent\n\n"
            "Output:\nYes"
        ),
    
        "test_cases": [
            {"input": "listen\nsilent\n", "expected_output": "Yes"},
            {"input": "hello\nworld\n", "expected_output": "No"},
            {"input": "Dormitory\ndirtyroom\n", "expected_output": "Yes"},
            {"input": "abc\nabcd\n", "expected_output": "No"},
        ],
    },
    {
        "title": "Check Palindrome String",
        "description": (
            "Read a string. Print 'Yes' if it reads the same forwards "
            "and backwards (ignoring case), otherwise print 'No'.\n\n"
            "Example:\n"
            "Input:\nMadam\n\n"
            "Output:\nYes"
        ),
        "test_cases": [
            {"input": "Madam\n", "expected_output": "Yes"},
            {"input": "Hello\n", "expected_output": "No"},
            {"input": "Racecar\n", "expected_output": "Yes"},
            {"input": "Python\n", "expected_output": "No"},
        ],
    },
    {
        "title": "Count Vowels and Consonants",
        "description": (
            "Read a string (may contain spaces). Print the number of "
            "vowels on the first line and the number of consonants on "
            "the second line. Only count alphabet letters (ignore "
            "spaces, digits, punctuation).\n\n"
            "Example:\n"
            "Input:\nHello World\n\n"
            "Output:\n3\n7"
        ),
        "test_cases": [
            {"input": "Hello World\n", "expected_output": "3\n7"},
            {"input": "Programming\n", "expected_output": "3\n8"},
            {"input": "AEIOU\n", "expected_output": "5\n0"},
        ],
    },
    {
        "title": "Banking System (Deposit & Credit)",
        "description": (
            "Step 1: Read the starting balance (a number).\n"
            "Step 2: Read a single letter - 'D' or 'C'.\n"
            "     'D' means Deposit (add money)\n"
            "     'C' means Credit (also add money - same as deposit)\n"
            "Step 3: Read the amount (a number) to add.\n"
            "Step 4: Add the amount to the balance.\n"
            "Step 5: Print the final balance.\n\n"
            "Example:\n"
            "Input:\n"
            "100\n"
            "D\n"
            "50\n\n"
            "Meaning: starting balance is 100, choice is Deposit, amount is 50.\n"
            "Output:\n"
            "150"
        ),
        
        "test_cases": [
            {"input": "100\nD\n50\n", "expected_output": "150"},
            {"input": "200\nC\n30\n", "expected_output": "230"},
            {"input": "0\nD\n1000\n", "expected_output": "1000"},
            {"input": "500\nC\n250\n", "expected_output": "750"},
        ],
    },
]