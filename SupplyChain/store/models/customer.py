from django.db import models

class Customer(models.Model):
    
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    E_mail = models.EmailField(default="abc@gmail.com")
    Password = models.CharField(max_length=500,default="none")

    def register(self):
        self.save()

    def account_exists(self):
        #if Customer.objects.filter(E_mail = self.E_mail):
        sql = (''' select * from store_customer where "E_mail"=%s ''')
        if Customer.objects.raw(sql,[self.E_mail]):
            return True
        
        return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            #return Customer.objects.get(E_mail = email)
            sql = ''' select * from store_customer where "E_mail"=%s '''
            return Customer.objects.raw(sql,[email])
        except:
            return False
           