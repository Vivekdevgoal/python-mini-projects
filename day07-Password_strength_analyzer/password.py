import os
import csv
import random

#-------------Scoring Weight------------#
Length={
    "short": 5,
    "medium": 10,
    "strong": 30,
    "very strong": 40
    }

Variety_Score = {
    "uppercase": 10,
    "lowercase": 10,
    "special_character": 20,
    "number": 20
    }

Penalties = {
    "repetition": 10,
    "sequence": 10,
    "keyboard":  10
    }

COMMON_PASSWORDS = [
    "password",
    "admin",
    "qwerty",
    "welcome",
    "letmein",
    "123456",
    "abc123",
    "iloveyou",
    "password123"
]

#------------confiurations--------------#
def pass_len(password):
    length = len(password)
    score = 0
    issues = []
    suggestions = []

    if  length < 8:
        score = Length["short"]
        issues.append("password is too short.")
        suggestions.append("use atleast 8 chaaracters.")        

    elif 8 <= length < 12:
        score = Length["medium"]
        issues.append("password is bit short.")
        suggestions.append("use >12 chaaracters.")
           
    elif 12 <= length < 16:
        score = Length["strong"]
        suggestions.append("Much good if use >12 chaaracters.")
        
    else:
        score = Length["very strong"]
    
    return score, issues, suggestions 
    
def has_sequential_pattern(password, min_length=3):
    count = 1

    for i in range(1, len(password)):
        prev = password[i - 1].lower()
        curr = password[i].lower()

        # Convert characters to positions
        if prev.isalpha() and curr.isalpha():
            prev_pos = ord(prev) - ord('a')
            curr_pos = ord(curr) - ord('a')

        elif prev.isdigit() and curr.isdigit():
            prev_pos = int(prev)
            curr_pos = int(curr)

        else:
            count = 1
            continue

        # Check forward or reverse sequence
        if curr_pos - prev_pos == 1 or curr_pos - prev_pos == -1:
            count += 1
            if count >= min_length:
                return True
        else:
            count = 1

    return False

def has_repeated_characters(password, min_repeats=3):
    count = 1

    for i in range(1, len(password)):
        if password[i].lower() == password[i - 1].lower():
            count += 1
            if count >= min_repeats:
                return True
        else:
            count = 1

    return False

def has_keyboard_pattern(password, min_length=3):
    password = password.lower()

    keyboard_rows = [
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    ]

    for row in keyboard_rows:
        for i in range(len(row) - min_length + 1):
            seq = row[i:i + min_length]

            if seq in password or seq[::-1] in password:
                return True

    return False

def has_dictionary_pattern(password):
    password = password.lower()

    for word in COMMON_PASSWORDS:
        if word in password:
            return True

    return False

def has_lowercase(password):
    for ch in password:
        if ch.lower():
            return True
    return False

def has_uppercase(password):
    for ch in password:
        if ch.upper():
            return True
    return False

def has_digit(password):
    for ch in password:
        if ch.isdigit():
            return True
    return False

def has_special(password):
    for ch in password:
        if not ch.isalnum():   # alphanumeric = letters + digits
            return True
    return False
    
def unique_char_ratio(password):
    if len(password) == 0:
        return 0.0

    unique_chars = set(password)
    return len(unique_chars) / len(password)

def max_char_frequency(password):
    freq = {}

    for ch in password:
        freq[ch] = freq.get(ch, 0) + 1

    return max(freq.values()) if freq else 0

#------------analysis functions---------#
def analyze_variety(password):
    score = 0
    issues = []
    suggestions = []

    if has_lowercase(password):
        score += Variety_Score["lowercase"]
    else:
        issues.append("No lowercase letters")
        suggestions.append("Add lowercase letters")

    if has_uppercase(password):
        score += Variety_Score["uppercase"]
    else:
        issues.append("No uppercase letters")
        suggestions.append("Add uppercase letters")

    if has_digit(password):
        score += Variety_Score["number"]
    else:
        issues.append("No digits")
        suggestions.append("Add numbers")

    if has_special(password):
        score += Variety_Score["special_character"]
    else:
        issues.append("No special characters")
        suggestions.append("Add special characters")

    return score, issues, suggestions

def analyze_patterns(password):
    score = 0
    issues = []
    suggestions = []
    if has_sequential_pattern(password, min_length=3):
        score -= Penalties["sequence"]
        issues.append("used sequences ")
        suggestions.append("use random characters")

    if has_repeated_characters(password, min_repeats=3):
        score -= Penalties["repetition"]
        issues.append("used repeated characters")
        suggestions.append("use unique characters")

    if has_keyboard_pattern(password, min_length=3):
        score -= Penalties["keyboard"]
        issues.append("used keyboard pattern")
        suggestions.append("dont use keyboard sequences.")

    if has_dictionary_pattern(password):
        score -= Penalties["repetition"]
        issues.append("used frequent pasword")
        suggestions.append("use unique password")

    return score, issues, suggestions 
#------------analysis engine------------#
def strength_analyzer(password):
    score_final = 0
    issues_final = []
    suggestions_final = []
    score1, issues1, suggestions1 = analyze_patterns(password)
    score2, issues2, suggestions2 = analyze_variety(password)
    score3, issues3, suggestions3 = pass_len(password)

    score_final = score1 + score2 + score3

    issues_final.extend(issues1)
    issues_final.extend(issues2)
    issues_final.extend(issues3)

    suggestions_final.extend(suggestions1)
    suggestions_final.extend(suggestions2)
    suggestions_final.extend(suggestions3)

    return score_final, issues_final, suggestions_final 

#------------aggregation function-------#
def classify_strength(score):
    if score < 30:
        return "Weak"
    elif score < 60:
        return "Moderate"
    elif score < 80:
        return "Strong"
    else:
        return "Very Strong"


#------------main function--------------#
def main():
    password = input("Enter a password to check its strength: ")
    score, issues, suggestion = strength_analyzer(password)

    print("\nPassword Strength:", classify_strength(score))
    print("Score:", score, "/ 100")

    if issues:
        print("\nIssues:")
        for issue in issues:
            print("-", issue)

    if suggestion:
        print("\nSuggestions:")
        for suggestion in suggestion:
            print("-", suggestion)

if __name__ == "__main__":
    main()
