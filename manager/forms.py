from django import forms  

class CategoryForm(forms.Form):
    name = forms.CharField(label="Category Name",max_length=200,min_length=1,required=True)
    image = forms.CharField(widget=forms.Textarea,required=False)




class DishForm(forms.Form):
    name = forms.CharField(label="Dish Name",max_length=200,min_length=1,required=True)
    price = forms.IntegerField(min_value=1,required=True)
    description = forms.CharField(widget=forms.Textarea,required=False)
    image = forms.CharField(widget=forms.Textarea,required=False)
    is_gluten_free = forms.BooleanField(required=False)
    is_vegeterian = forms.BooleanField(required=False)