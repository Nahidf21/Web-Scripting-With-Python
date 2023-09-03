import requests as r  # Importing the requests library to make HTTP requests
from bs4 import BeautifulSoup  # Importing the BeautifulSoup library for web scraping

base_url = "http://drd.ba.ttu.edu/isqs6339/labs/lab1/"  # Defining the base URL to scrape
response = r.get(base_url)  # Making an HTTP GET request to the base URL
soup = BeautifulSoup(response.content, 'lxml')  # Parsing the returned content with BeautifulSoup

y = soup.find_all("li")  # Finding all list item tags in the parsed content

# Iterating through each list item tag
for li_element in y:
    span_element = li_element.find("span")  # Finding the first span tag within the current list item

    # Checking if the span tag exists and if the word "iPhone" is within its text
    if span_element and "iPhone" in span_element.text:
        link_element = li_element.find("a")  # Finding the first anchor tag within the current list item

        # Checking if the anchor tag exists
        if link_element:
            iphone_link = link_element["href"]  # Extracting the href attribute (the link)
            full_url = base_url + iphone_link  # Constructing the full URL by combining the base URL and the extracted link
            response = r.get(full_url)  # Making an HTTP GET request to the constructed URL

            #print("iPhone Link:", full_url)

            x = BeautifulSoup(response.content, "lxml")  # Parsing the returned content for the individual iPhone page

            # Extracting storage information
            storage_tag = x.find("td", string="Storage:  ")  # Finding the table data cell with "Storage:  " string
            # Checking if the storage tag was found
            if storage_tag:
                # Finding the next sibling of the storage tag which has the class "item"
                storage_value = storage_tag.find_next_sibling("td", class_="item")
                # Checking if the storage value was found
                if storage_value:
                    print("Storage:", storage_value.text.strip())  # Printing the storage information

            # Extracting front camera features
            front_camera_tag = x.find("span", string="Camera Front:")  # Finding the span with "Camera Front:" string
            # Checking if the front camera tag was found
            if front_camera_tag:
                # Finding the next sibling of the front camera tag which has the class "item"
                front_camera_features = front_camera_tag.find_next_sibling("span", class_="item")
                # Checking if the front camera features were found
                if front_camera_features:
                    features_list = front_camera_features.find(
                        "ul")  # Finding the unordered list tag within the features span
                    # Checking if the features list was found
                    if features_list:
                        # Extracting the text of each list item within the features list
                        features = [li.text for li in features_list.find_all("li")]
                        print("Front Camera Features:", ", ".join(features))  # Printing the front camera features

