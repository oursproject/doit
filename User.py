import time
class User(object):
    """A user class with typical attributes like name,phone,email etc"""
    def __init__(self):
        self.dob = time.strftime("%d/%m/%Y")
        print self.__doc__

    def get(self):
        self.age = int(raw_input('Enter the age: '))
        self.firstName = str(raw_input('Enter the firstname: '))
        self.middleName = str(raw_input('Enter the middlename: '))
        self.lastName = str(raw_input('Enter the lastname: '))
        self.sex = str(raw_input('Enter the Gender: '))
        self.phone = int(raw_input('Enter the mobile number: '))
        self.mobile = int(raw_input('Enter the phone number: '))
        self.email = str(raw_input('Enter the email-id: '))
        self.dob =  str(raw_input('Enter the dob: '))
        #contact = Contacts()
    def dis(self):
        print "Name: %s %s %s\nAge: %d\nSex:%s\nPhone:%d\n" %(self.firstName,self.middleName,self.lastName,self.age,self.sex,self.phone),
        print "Mobile:%d\nEmail:%s\nDob:%s" % (self.mobile,self.email,self.dob)
        contact = Contacts()
        print "Facebook id: %s\nTwitter id: %s\nGoogle+ id:%s" % (contact.facebook_id,contact.twitter_id,contact.googleplus_id)
        

class Contacts(object):
    
    def __init__(self):
        self.facebook_id = str(raw_input('Enter facebook id: '))    
        self.twitter_id = str(raw_input('Enter twitter id: '))
        self.googleplus_id = str(raw_input('Enter google+ id: '))
    
             
manoj = User()
manoj.get()
manoj.dis()
#obj=Contacts()
