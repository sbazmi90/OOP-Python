class Contact:

    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def display_contact(self):
        return f"Name: {self.name}\n Phone: {self.phone_number}\n Email: {self.email}"



class BusinessContact(Contact):

    def __init__(self, name, phone_number, email, business_name):
        super().__init__(name, phone_number, email)
        self.business_name = business_name

    def display_business_contact(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nBusiness Name: {self.business_name}"




c = Contact("John Doe", "709-220-2222", "jdoe@mail.com")
print(c.display_contact())

bc = BusinessContact("Jane Doe", "+1-987-654-3210", "jane.doe@example.com", "Acme Inc.")
print(bc.display_business_contact())