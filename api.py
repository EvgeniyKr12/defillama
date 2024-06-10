from faker import Faker
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import RedirectResponse
from database.select import get_data_in_db
from database.insert_user import insert_data_mysql


app = FastAPI()
faker = Faker()


@app.get("/")
async def read_root(request: Request):
    return RedirectResponse(f"{request.url}docs")


def get_users():
    users = {}
    user_all = get_data_in_db('users', '*')

    for user in user_all:
        users[user["user_id"]] = user["name"]

    return users


@app.get("/ethereum/tvl")
async def get_ethereum_tvl():
    total_value_locked = get_data_in_db('ethereum', '*')[-1]
    users_in_db = get_users()
    authorized_users = [user for user in users_in_db.keys()]
    return {"latest update": total_value_locked['data'], "total_value_locked": total_value_locked['value'], "info" : authorized_users}


@app.get("/user/{user_id}/ethereum/tvl")
async def get_ethereum_tvl_for_user(user_id: str):
    print("Received user_id:", user_id)
    users_in_db = get_users()
    authorized_users = [user for user in users_in_db.keys()]

    if user_id not in authorized_users:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User not authorized",
        )

    total_value_locked = get_data_in_db('ethereum', '*')[-1]
    return {"latest_update": total_value_locked['data'], "total_value_locked": total_value_locked['value'], 'user_name': users_in_db[user_id]}


def verify_token(token):
    if token != "vVnX3jabqrFmz??eGxD2fceOAgCeFN?y9AdsTAHwP3Qb44-NVDFn!3B3kw6KD2CAEosy6vLNeCRZMxun":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@app.post("/admin/adduser")
async def create_admin_data(request: Request):
    json_data = await request.json()
    token = json_data.get("token")
    data = json_data.get("data")
    verify_token(token)

    insert_data_mysql('users', [data['name'], data['user_id']])
    return {"message": "Data inserted successfully", "data": data}



