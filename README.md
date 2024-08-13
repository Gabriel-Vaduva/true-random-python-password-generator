This is a True password generator that uses this python function 

********************************************

   random.seed(time.time())
    password = "".join(random.choice(chars) for _ in range(length))
    return password

********************************************

to generate password 

This is designed to run in docker container and can be accesed via web browser on port 5000