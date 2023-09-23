from django.forms import ModelForm
#here we created a form of todo model..
from app.models import TODO
class TODOForm(ModelForm):
    #class meta is used for linking the model with the form..
    class Meta:
        model = TODO
        fields = ['title' , 'status' , 'priority']