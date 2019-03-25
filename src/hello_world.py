def shout(body):
    print(body["message"])
    res = {"Result_message": body["message"],
            "additional_info": "toller code"}
    return(res)
