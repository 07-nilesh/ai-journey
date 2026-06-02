import requests

# --- Example 1: GET Request ---
# We are asking the server to fetch an existing post. No payload is needed.
get_url = "https://jsonplaceholder.typicode.com/posts/5"

get_response = requests.get(get_url)
print("GET Output:", get_response.json())


# --- Example 2: POST Request ---
# We are asking the server to create a brand new post.
post_url = "https://jsonplaceholder.typicode.com/posts"

# The Payload: The actual data we want the server to create and save
new_post_data = {
    "title": "Nilesh",
    "body": "Learning REST APIs today!",
    "userId": 1
}

# We use requests.post() and pass our payload to the 'json' parameter
post_response = requests.post(post_url, json=new_post_data)
print("POST Output:", post_response.json())

# variation 1
get_url_1="https://jsonplaceholder.typicode.com/users"
get_response_1=requests.get(get_url_1)
print("GET Output:", get_response_1.json())

# variation 2
put_url ="https://jsonplaceholder.typicode.com/posts/1"
updated_post_data = {"title":"Python Master"}
put_response = requests.put(put_url, json=updated_post_data)
print("PUT Output:", put_response.json())

# Assume this URL returns a list of 100 items
url = "https://jsonplaceholder.typicode.com/posts" 
response = requests.get(url)
data = response.json()
print(type(data))

import requests
target_id = 77
response = requests.get(f"https://api.com/products/{target_id}")
print(response.json())
