contacts = {
    "contact_1": {
        "name": "Anna Ivanova",
        "phone": "0586774354",
        "email": "anna.Ivanova@mail.com"
    },
    "contact_2": {
        "name": "Petr Sidorov",
        "phone": "0586774353",
        "email": "Petr.Sidorov@mail.com"
    }

}

# print(contacts["contact_1"])

contacts["contact_2"]["phone"] = "+79225551122"
print(contacts["contact_2"])

contacts["contact_1"]["adress"] = "Москва, ул. Пушкина, д.10"
print(contacts["contact_1"])

del contacts["contact_2"]["email"]
print(contacts)