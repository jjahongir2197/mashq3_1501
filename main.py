class GymMember:
    def __init__(self, name, days):
        self.name = name
        self.days_left = days

    def attend(self):
        if self.days_left > 0:
            self.days_left -= 1
            return f"Mashg‘ulot bajarildi. Qolgan kunlar: {self.days_left}"
        return "Obuna tugagan"

    def extend(self, days):
        self.days_left += days
        return f"Obuna {days} kunga uzaytirildi"

    def status(self):
        return f"{self.name} | Qolgan kunlar: {self.days_left}"


member = GymMember("Jahongir", 12)
print(member.attend())
print(member.extend(10))
print(member.status())
