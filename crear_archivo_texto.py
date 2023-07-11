

CONTACTS = [
    {"name": "contact 1", "apellido": "apellido 1", "numero": "1"},
    {"name": "contact 2", "apellido": "apellido 2", "numero": "2"},
    {"name": "contact 3", "apellido": "apellido 3", "numero": "3"}
]

DELIMITER = ","

with open("contacts.txt", "w") as file:
    for contact in CONTACTS:
        file.write(f"{DELIMITER.join(contact.values())}\n")

