from django import forms  

class DeliveryForm(forms.Form):
    address = forms.CharField(label="Address",max_length=200,min_length=1,required=True)
    comment = forms.CharField(widget=forms.Textarea,required=False)