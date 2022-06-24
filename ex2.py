def change_pwd(d: dict):
    for k, v in d.items():
        if k == "password":
            n = len(v)
            newpass = ""
            for i in range(0, n):
                newpass = newpass + "*"
            d[k] = newpass
        elif isinstance(v, dict):
            change_pwd(v)
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    change_pwd(i)
                else:
                    continue


d = {
    "servers": [
        {
            "mongo": {
                "host": "10.100.0.1",
                "credentials": {
                    "user": "admin",
                    "password": "1234567890"
                }
            }
        },
        {
            "redis": {
                "host": "127.0.0.1",
                "user": "redis",
                "password": "sgdsgdgs"
            }
        },
        {
            "mariadb": {
                "host": "mariadb.hfmarkets.com",
                "user": "dbmaster",
                "password": "strong_password123!"
            }
        }
    ]
}

change_pwd(d)
print(d)
