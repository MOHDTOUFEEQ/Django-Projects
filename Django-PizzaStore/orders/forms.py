from django import forms
from .models import Pizza , Size
from django.core.exceptions import ValidationError
# class pizzaform(forms.Form):
#     topping1 = forms.CharField(label="Topping 1", max_length=200)
#     topping2 = forms.CharField(label="Topping 2", max_length=200)
#     size = forms.ChoiceField(label="size", choices=[("Small","Small"),("Medium","Medium"),("Large","Large")])


class pizzaform(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["topping1","topping2","size"]
        labels = {"topping1":"Topping  1","topping2":"Topping  2"}
    def clean_title(self):
        top1 = self.cleaned_data["topping1"]
        if "@" not in top1:
            raise ValidationError("we accept only @ value in the form")
        return top1

class myy(forms.Form):
    name = forms.CharField(label="name", max_length=200)
    phone = forms.CharField(label="phone_number", max_length=200)

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2,max_value=6)

class my_form(forms.Form):
    num = forms.IntegerField(max_value=10,min_value=1)