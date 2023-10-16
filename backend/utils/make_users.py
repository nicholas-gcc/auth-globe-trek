import json
import random

users = []

for i in range(1):
    user = {
        "email": f"user{i}@test.com",
        "email_verified": False,
        "username": f"user{i}",
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
            # Note: We aren't directly setting 'lastIP' in app_metadata.
            "last_login_ip": f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        }
    }
    users.append(user)

with open("users.json", "w") as outfile:
    json.dump(users, outfile)
