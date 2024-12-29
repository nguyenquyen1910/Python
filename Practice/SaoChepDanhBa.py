class Contacts:
    def __init__(self, fullname, day, phone):
        self.fullname = fullname
        self.day = day
        self.phone = phone
        self.name = self.fullname.split()[-1]
        self.surname = " ".join(self.fullname.split()[:-1])

    def __str__(self):
        return f"{self.fullname}: {self.phone} {self.day}"

contacts = []
with open("SOTAY.txt", "r", encoding="utf-8") as file:
    day=""
    phone=""
    name=""
    for line in file:
        s = line.strip()
        if "Ngay" in s:
            day = s.split(" ")[1]
        elif s.startswith("0"):
            phone = s
            contact = Contacts(name, day, phone)
            contacts.append(contact)
        else:
            name = s

contacts.sort(key = lambda x: (x.name, x.surname))
with open("DIENTHOAI.txt", "w", encoding="utf-8") as file:
    for contact in contacts:
        file.write(str(contact)+"\n")