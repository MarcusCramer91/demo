def add(body):
    username = body["username"]
    password = body["password"]
    res = "Created user {} with password {}.".format(username, password)
    print(res)
    return res
