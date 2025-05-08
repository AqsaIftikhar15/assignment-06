class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_bank_name(self):
        print(f"Bank Name: {self.bank_name}")

customer1 = Bank()
customer1.display_bank_name()
Bank.change_bank_name("XYZ Bank")
customer1.display_bank_name()  
