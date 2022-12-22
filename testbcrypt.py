import bcrypt

passw = input('Введите ваш пароль ')
print(passw)
print(type(passw))
passw = str.encode(passw)
print(passw)
print(type(passw))
passw = str(passw)
print(passw)
print(type(passw))
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passw.encode('utf-8'),salt)
print(type(hashed))

if (bcrypt.checkpw(passw.encode('utf-8'),hashed)):
    print('match')
else:
    print('not match')