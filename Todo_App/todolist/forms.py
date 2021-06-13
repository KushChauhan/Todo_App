from django import forms
# from django.forms.forms import Form
from django.forms.widgets import Widget

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=50,
        widget = forms.TextInput( 
            attrs={'class' : 'form-control', 'placeholder' : 'Enter todo e.g. Grocery shopping', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))

