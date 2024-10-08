#how to connect to an API using python
'''
In Python, dictionaries and JSON (JavaScript Object Notation) both facilitate structured data representation, yet they diverge in usage and syntax. In this article, we will discuss the Definition of JSON and Dictionary and the difference between JSON and Dictionary in Python.

JSON vs Dictionary
Dictionaries, native to Python, are employed for in-memory data structures, allowing direct manipulation. In contrast, JSON serves as a standardized string-based format, vital for data exchange between systems.

Distinct in their data types, dictionaries offer in-memory flexibility, while JSON, with its string format, excels in interoperability. Below we will see differences in the form of a table.
In Python, dictionary values are not accessible using the my_dict.key syntax. This is reserved for attributes of the dict class, such as dict.get and dict.update. Dictionary values are only accessible via the my_dict[key] syntax.
'''
import requests
import os
os.environ["REQUESTS_CA_BUNDLE"] = '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/certifi/cacert.pem'
os.environ["SSL_CERT_FILE"] = '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/certifi/cacert.pem'
base_url="https://pokeapi.co/api/v2/"

# to get info abt pokemon from api

# To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark. Inside this string, you can \
# write a Python expression between { and } characters that can refer to variables or literal values.

def get_pokemon_info(name):
    url=f"{base_url}pokemon/{name}"
    print(url)
    response=requests.get(url)
    print(response) # jsut returns a http response code
    if response.status_code==200:
        pokemon_data=response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

name="pikachu"
pokemon_info=get_pokemon_info(name)

if pokemon_info:
    print(f"{pokemon_info['name']}")
    print(f"{pokemon_info['id']}")
    print(f"{pokemon_info['height']}")
    print(f"{pokemon_info['weight']}")