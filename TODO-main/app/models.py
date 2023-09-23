from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#  title 
#  status
#  date - current 
#  user 
#  priority

#here the models is module and the Model is  class and the User is also  class
class TODO(models.Model):
    status_choices = [
    ('C', 'COMPLETED'),
    ('P', 'PENDING'),
    ]
    priority_choices = [
    ('1', ''),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
    ('6', '6️⃣'),
    ('7', '7️⃣'),
    ('8', '8️⃣'),
    ('9', '9️⃣'),
    ('10', '🔟'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2 , choices=status_choices)
    #here User model is a foreign key which means the User tables are associated with the user field
    #on delete means that if if a user is  deleted then all todos are also deleted..
    user  = models.ForeignKey(User  , on_delete= models.CASCADE)
    #auto add states that it automatically adds todays date..
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10 , choices=priority_choices)

    # def __str__(self):
    #    return  "%s %s %s %s" %(self.user ,self.title, self.status,self.priority) 