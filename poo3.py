class Person:
    def __init__(self): # The constructor
        print("Calling constructor of class Person")
        self.name = "" # name will be an instance variable due to ’self’ keyword
        self.email_address = ""
    language = "French" # language will be a class variable (no self.)

    @staticmethod # get_language will be a class method using @staticmethod annotation
    def get_language():
        return Person.language
# print(get_language())

    @classmethod
    def set_language(cls,language):
        cls.language=language
    
    def get_name(self):
        return self.name
    
    def get_email_adress(self):
        return self.email_address
    
    def set_email_adress(self,email):
        self.email_address=email
    def display_data(self):
        print("Email for {} is {}".format(self.get_name(),self.get_email_adress()))
        print("Native spoken language is {}".format(self.language))
    
p1=Person()
p1.name="Anas"
p1.email_address="A.gmail.com"

print(p1.display_data())

#Classe et héritage : syntaxe par l’exemple avec le compte bancaire
# • Compte basique avec les opérations déposer et retirer un montant, connaitre le solde
# • Compte courant, dérivé du compte basique
# avec un découvert possible spécifique à chaque compte crée
# avec re-définition de l’opération ’retirer un montant’, tenant compte du découvert possible

class BankAccount():
    def __init__(self, owner):
# create account with a unique id,no amount
        self.id = id
        self.amount = 0
        self.owner = owner
        return # for readability
def deposit(self, amount):
    self.amount += amount
    return
def withdraw(self, amount):
    self.amount -= amount
    return
def get_id(self):
    return(self.id)
def get_amount(self):
    return(self.amount)
def get_owner(self):
    return(self.owner)  

a1=BankAccount("anas")
print(a1.amount)

deposit(a1,1000)
deposit(a1,1000)
withdraw(a1,500)
print(a1.amount)
print(get_owner(a1))

# Heritage
class CurrentAccount(BankAccount):
# *** CurrentAccount extends BankAccount
# new withdraw implementation according to min_amount allowed
# ***
# this is the constructor
    def __init__(self, owner):
# invoke constructor from super class
        BankAccount.__init__(self, owner)
# a new field specific to CurrentAccount
        self.min_amount = 0
        return
    def set_min_amount(self,min_amount):
        self.min_amount=min_amount
    def get_min_amount(self):
        return self.min_amount
    

    
    """ withdraw allowed only if min amount is not reached """
    # just to show : min_amount has a local scope
       
    def withdraw(self, amount):
        
        min_amount = self.amount - amount
        if (min_amount < self.min_amount):
            print("withdraw operation of {} Euros is denied since"
    " the low threshold of {} Euros "
    "would be reached !".format(amount, self.get_min_amount()))
        else:
    # case ok, invoke super class’s method
            BankAccount.withdraw(self, amount)
            return "retrait accepté, compte actuel {} ".format(self.amount-amount)
    # end of class CurrentAccount()
def main():
    bank_account=CurrentAccount("Amine")
    bank_account.set_min_amount(-20)
        # print("Bank account for {} is created with a low threshold of {} Euros" \
        #     .format(CurrentAccount.get_owner(), BankAccount.get_min_amount()))
    print("Bank account for {} is created with a low threshold of {} Euros" \
            .format(get_owner(bank_account), bank_account.get_min_amount()))
    deposit(bank_account,123)
    print("Current amount is {} Euros".format(get_amount(bank_account)))
    withdraw(bank_account,100)
    print("Current amount is {} Euros".format(get_amount(bank_account)))
    withdraw(bank_account,50)
    print("Current amount is {} Euros".format(get_amount(bank_account)))
if __name__=="__main__":
    main()


# bank_account=CurrentAccount("Amine")
# bank_account.set_min_amount(-20)
#     # print("Bank account for {} is created with a low threshold of {} Euros" \
#     #     .format(CurrentAccount.get_owner(), BankAccount.get_min_amount()))
# print("Bank account for {} is created with a low threshold of {} Euros" \
#         .format(get_owner(bank_account), bank_account.get_min_amount()))
# deposit(bank_account,123)
# print("Current amount is {} Euros".format(get_amount(bank_account)))
# withdraw(bank_account,100)
# print("Current amount is {} Euros".format(get_amount(bank_account)))
# withdraw(bank_account,50)
# print("Current amount is {} Euros".format(get_amount(bank_account)))
    
    
    
    