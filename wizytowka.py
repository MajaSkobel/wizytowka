from faker import Faker
fake = Faker()

contacts=[]

class BaseContact:
    def __init__(self,first_name,last_name,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self._label_length = len(self.first_name+" "+self.last_name)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email}"
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.phone_number}, {self.email}"
    
    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.first_name}.")

    @property
    def label_length(self):
        return self._label_length
    
class BusinessContact(BaseContact):
    def __init__(self,company,job,work_phone_number,*args,**kwargs):
       super().__init__(*args, **kwargs)
       self.company = company
       self.job = job
       self.work_phone_number = work_phone_number

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.phone_number}, {self.email}, {self.job}, {self.company}, {self.work_phone_number}"
       
    def contact(self):
        print(f"Wybieram numer {self.work_phone_number} i dzwonię do {self.first_name} {self.first_name}.")

def create_contacts(card_type,quantity):
    if card_type == "Base":
        for i in range(quantity):
            contacts.append(BaseContact(fake.first_name(),fake.last_name(),fake.phone_number(),fake.email()))
    elif card_type == "Business":
        for i in range(quantity):
            contacts.append(BusinessContact(first_name=fake.first_name(),last_name=fake.last_name(),phone_number=fake.phone_number(),email=fake.email(),job=fake.job(),company=fake.company(),work_phone_number=fake.phone_number())) 

create_contacts("Business",5)
print(contacts)