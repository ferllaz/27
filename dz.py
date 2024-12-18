import aiohttp
import asyncio
import json

fname = "json_files"

def create_folder(folder_name):
    open(f"{folder_name}/.placeholder", "w").close()

async def fetch_data(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()

async def save_json_objects():
    url = "https://jsonplaceholder.typicode.com/users"
    create_folder(fname)

    async with aiohttp.ClientSession() as session:
        data = await fetch_data(session, url)

        if data:
            with open(f"{fname}/user_1.json", "w") as file:
                json.dump(data[0], file, indent=4)
            with open(f"{fname}/user_2.json", "w") as file:
                json.dump(data[1], file, indent=4)
            with open(f"{fname}/user_3.json", "w") as file:
                json.dump(data[2], file, indent=4)
            with open(f"{fname}/user_4.json", "w") as file:
                json.dump(data[3], file, indent=4)
            with open(f"{fname}/user_5.json", "w") as file:
                json.dump(data[4], file, indent=4)
            with open(f"{fname}/user_6.json", "w") as file:
                json.dump(data[5], file, indent=4)
            with open(f"{fname}/user_7.json", "w") as file:
                json.dump(data[6], file, indent=4)
            with open(f"{fname}/user_8.json", "w") as file:
                json.dump(data[7], file, indent=4)
            with open(f"{fnam}/user_9.json", "w") as file:
                json.dump(data[8], file, indent=4)
            with open(f"{fname}/user_10.json", "w") as file:
                json.dump(data[9], file, indent=4)

            print("JSON-объекты успешно сохранены в папке", fname)

asyncio.run(save_json_objects())
