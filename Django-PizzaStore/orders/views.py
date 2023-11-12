from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import pizzaform , MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza
# Create your views here.

def home(request):
    return render(request,"home.html",{})
def order(request):
    multiple_form = MultiplePizzaForm
    if request.method == "POST":
        filled_form = pizzaform(request.POST)
        if filled_form.is_valid():
            object=  filled_form.save()
            object_pk = object.id
            note = "thankyou for ordering the pizza %s %s and %s , it on the way" %(filled_form.cleaned_data["topping1"],
                filled_form.cleaned_data["topping2"],
                filled_form.cleaned_data["size"])
            new_form = pizzaform
            edit = "wanna edit"
            return render(request,"order.html",{"pizzaform" : new_form,"note":note ,"multiple_form" : multiple_form,"edit":edit,"object_pk":object_pk})
    else:
        form = pizzaform
    return render(request,"order.html",{"pizzaform" : form , "multiple_form":multiple_form})


def pizzas(request):
    no_of_pizz = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        no_of_pizz = filled_multiple_pizza_form.cleaned_data["number"]
    PizzaForSet = formset_factory(pizzaform, extra=no_of_pizz)
    formset = PizzaForSet()
    if request.method == 'POST':
        filled_formset = PizzaForSet(request.POST)
        if (filled_formset.is_valid()):
            for form in filled_formset:
                form.save()
            note =  "you have ordered a pizza"
        else:
            note =  "ordered has an error"
        
        
        return render(request,"pizza.html",{"note":note,"formset":formset})
    else:
        return render(request,"pizza.html",{"formset":formset})



def edit_order(request,pk):
    backend_data = Pizza.objects.get(pk = pk)
    form = pizzaform(instance=backend_data)
    if request.method == "POST":
        get_data = pizzaform(request.POST,instance=backend_data)
        if get_data.is_valid():
            get_data.save()
            note = "edited successfully"
            form = get_data
        return render(request,"edit.html",{'form':form,"backend_data":backend_data,"note":note})
    else:
        return render(request,"edit.html",{'form':form,"backend_data":backend_data})
            
    


