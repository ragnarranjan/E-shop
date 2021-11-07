from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=30)


    def __str__(self):
        return self.first_name

    
    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)#-------our email during login time email nd cutomer model email will matched here if matched k eitherwise 
        except:
            return False
#here we can use ---Customer.objects.filter(email = email)  but it gives a querryset  
# but .get() -- method will give single object so we r using it
# we r using try except bcz  .get --method will give error if there is no customer with that
#  email for which we r checking  but .filter -- return NONE so error will nt cme 