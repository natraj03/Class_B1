import requests

url = "https://dummyjson.com/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    users = data.get("users",[])

    print("user id - city")

    for u in users:
        user_id = u.get('id')

        city = u.get("address",{}).get("city")

        print(f"{user_id} : {city}")

else:
    print('failed to fetch data')

