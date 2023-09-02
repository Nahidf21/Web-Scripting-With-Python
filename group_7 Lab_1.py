# Import necessary libraries
import requests as r
from bs4 import BeautifulSoup

# Specify the URL to be fetched
url = 'http://drd.ba.ttu.edu/isqs6339/labs/lab1/'

# Make a GET request to the URL
res = r.get(url)

# Check if there was a redirect when accessing the URL
is_redirecting = res.history

# Parse the content of the response using BeautifulSoup
soup=BeautifulSoup(res.content,'html')

# Print output for Task #1
print("Value for Task #1 ")

# Display the HTTP status code of the response
print(f"Status Code of call :  {res.status_code}")

# Check and display if the page is redirecting
print(f"Page is Redirecting : {bool(is_redirecting)}")

# Display the encoding of the page
print(f"Current page Encoding : {res.encoding} ")

# Display headers returned by the server
print(res.headers,"\n")

# Print output for Task #2
print("***Task #2**")

# Find the div element with id "phonelist" from the parsed HTML
search_result = soup.find('div', attrs={"id": "phonelist"})

# Locate the span element with text 'iPhone 11 Pro'
iphone_element = soup.find('span', text='iPhone 11 Pro')

# Check if the iPhone 11 Pro span element was found
if iphone_element:
    # Find the parent 'li' tag of the span element
    parent_li = iphone_element.find_parent('li', class_='root')

    # Get all list item tags within the parent list
    details = parent_li.find_all('li')

    # Iterate over the list items to find and display the color and OS
    for detail in details:
        if 'Color:' in detail.text:
            color = detail.text.split(': ')[1]
        if 'OS:' in detail.text:
            os = detail.text.split(': ')[1]

    # Display the extracted details for iPhone 11 Pro
    print("The following are values for the iphone 11 Pro")
    print('Color:', color)
    print('OS:', os)
else:
    # If the span for iPhone 11 Pro was not found, display a message
    print("iPhone 11 Pro not found.")

print("***Task #3**")

