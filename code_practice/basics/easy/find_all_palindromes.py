def find_palindromes(text):
    words = text.split()
    return [word for word in words if word == word[::-1]]

# Example Usage
print(find_palindromes("madam level radar hello world"))
# Output: ['madam', 'level', 'radar']
