# Example for the use of quoting and unquoting URLs

from urllib.parse import quote, unquote

print(f"In a URL, the letter & is written as {quote('&')}")
print(f"If you see %2B in a URL, it represents the letter {unquote('%2B')}")
