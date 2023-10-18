import json
import random

def generate_base_ips(num):
    return [f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}" for _ in range(num)]

def get_ip_from_base(base_ips):
    base_ip = random.choice(base_ips)
    return f"{base_ip}.{random.randint(0, 255)}"

users = []
BASE_IP_COUNT = 10
BASE_IP_CHANCE = 0.7
base_ips = generate_base_ips(BASE_IP_COUNT)

for i in range(100):
    if random.random() < BASE_IP_CHANCE:
        last_login_ip = get_ip_from_base(base_ips)
    else:
        last_login_ip = f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

    user = {
        "email": f"user{i}@test.com",
        "email_verified": False,
        "given_name": f"User",
        "family_name": f"#{i}",
        "name": f"User #{i}",
        "nickname": f"user{i}",
        "app_metadata": {
            "roles": ["admin"] if i % 2 == 0 else ["user"],
            "plan": "premium"
        },
        "user_metadata": {
            "theme": "light",
            "last_login_ip": last_login_ip
        }
    }
    users.append(user)

with open("users.json", "w") as outfile:
    json.dump(users, outfile)

