class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
    
    def deposit(self, amount, description = ""):
        dic = {"amount": amount, "description": description}
        self.ledger.append(dic)
        self.balance += amount

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            dic = {"amount": -amount, "description": description}
            self.ledger.append(dic)
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination):
        if (self.check_funds(amount)):
            description = "Transfer to " + destination.name
            self.withdraw(amount, description)
            description = "Transfer from " + self.name
            destination.deposit(amount, description)
            return True
        else:
            return False
    
    def __str__(self):
        display = ""
        display += f"{self.name:*^30}\n"
        for transaction in self.ledger:
            description = transaction["description"]
            description = description[:23]
            temp_str = f"{description:<23}"
            amount = transaction["amount"]
            temp_str += f"{amount:>7.2f}\n"
            display += temp_str
        display += f"Total: {self.balance}"
        return display


def create_spend_chart(categories):
    display = "Percentage spent by category\n"
    withdrawals = []
    names = []
    for category in categories:
        amount = 0
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                amount -= transaction["amount"]
        withdrawals.append(amount)
        names.append(category.name)
    amount = sum(withdrawals)
    percentages = []
    for i in range(len(withdrawals)):
        perc = (withdrawals[i] / amount) // 0.1
        perc = round(perc) * 10
        percentages.append(perc)
    
    for perc in range(100, -1, -10):
        display += f"{perc:>3}" + "| "
        for i in range(len(percentages)):
            if percentages[i] < perc:
                display += "   "
            else:
                display += "o  "
        display += "\n"
    display += "    -" + (3 * len(percentages) * "-") + "\n"
    longest_string = max(names, key=len)
    for i in range(len(longest_string)):
        display += "     "
        for name in names:
            if i < len(name):
                display += name[i] + "  "
            else:
                display += "   "
        if i < (len(longest_string) - 1):
            display += "\n"

    return display
