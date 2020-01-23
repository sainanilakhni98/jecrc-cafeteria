from django import forms

class Showdata(forms.Form):
    product_name = forms.CharField(max_length=40)
    product_ratings=forms.CharField(max_length=40)
    comment =forms.CharField(max_length=200)
    
   