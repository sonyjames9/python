import re

def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

# Example Usage
text = "Contact us at support@example.com or info@domain.net."
print(extract_emails(text))  # Output: ['support@example.com', 'info@domain.net']


"""
doubts to check

set(string.ascii_lowercase).issubset(set(s.lower()))
return all(c in s.lower() for c in string.ascii_lowercase)
return len(set(re.findall(r'[a-z]', s.lower()))) == 26
return dict(Counter(words))
return [item for sublist in nested_list for item in (flatten_list(sublist) if isinstance(sublist, list) else [sublist])]
return [pair for pair in combinations(out_list, 2) if sum(pair) == expected_sum]
return list(map(list, zip(*matrix)))
return Counter(lst).most_common(1)[0] if lst else (None, 0)
return list(map(list, zip(*matrix)))


# READ YOUR RESUME    **********
# AND ALL DOWNLOADED DOCS ESPECIALLY OF K8S BEFORE BMC INTERVIEW  **********
# ALSO CHECK PLAYWRIGHT- HOW ITS USED ******
# SELENIUM AS WELL      **********
"""