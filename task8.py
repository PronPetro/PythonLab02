phone="+38(099)-123-12-13"

print(phone)

phone = phone.replace("-", "")
phone = phone.replace("+", "")
phone = phone.replace("(", "")
phone = phone.replace(")", "")

print(phone)