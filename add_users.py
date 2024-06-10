import requests


def add_user_in_db(name, user_id):
    url = "http://127.0.0.1:8000/admin/adduser"

    payload = {
        "token": "vVnX3jabqrFmz??eGxD2fceOAgCeFN?y9AdsTAHwP3Qb44-NVDFn!3B3kw6KD2CAEosy6vLNeCRZMxun",
        "data": {
            "name": name,
            "user_id": user_id
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Data inserted successfully:", response.json())
    else:
        print("Failed to insert data. Status code:", response.status_code, "Response:", response.json())


if __name__ == '__main__':
    add_user_in_db("Kravchenko Eugene", "1050406")
