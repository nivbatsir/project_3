from django import forms     
    
  
class CustomUserCreationForm(forms.Form):  
    username = forms.CharField(min_length=1, max_length=150,required=True)  
    email = forms.EmailField(required=True)  
    password = forms.CharField(min_length=1, max_length=150,required=True) 
    first_name = forms.CharField(max_length=30,min_length=1,required=True)
    last_name = forms.CharField(max_length=30,min_length=1,required=True) 
    is_staff = forms.BooleanField(required=False)

   
class CustomUserLoginForm(forms.Form):
    username = forms.CharField(min_length=1, max_length=150,required=True)
    password = forms.CharField(min_length=1, max_length=150,required=True)
   
    
    


   
