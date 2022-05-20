from django import forms

class CreateNewItem(forms.Form):
    item_name = forms.CharField(label="Item Name", max_length=200, required=False)
    item_number = forms.CharField(label="Item Number", max_length=200)
    # number = forms.BigIntegerField()
    # check = forms.BooleanField(required=False)