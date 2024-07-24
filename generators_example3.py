import requests

def fetch_url(url):
    """A generator function to fetch data from a URL line by line."""
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an error for bad status codes

    for line in response.iter_lines():
        if line:
            yield line.decode('utf-8')

# Example usage
url = 'https://example.com/largefile.txt'
for line in fetch_url(url):
    print(line.strip())

# generators will remember the line it stopped at the last yield.
# This is one of the key features of generators in Python: they maintain their state between calls.
# When you call next() on the generator, it resumes execution right after the last yield statement.