from django import forms
from .models import ToDoList, ToDoItem


class ToDoItemForm(forms.ModelForm):
    todo_list = forms.ModelChoiceField(
        queryset=ToDoList.objects.all(),
        label='Lista ToDo',
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
    title = forms.CharField(
        label='Título',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Título",
                "class": "form-control col-md-8",
                "type": "text"
            }
        )
    )
    description = forms.CharField(
        label='Descrição',
        widget=forms.Textarea(
            attrs={
                'rows': '5'
            }
        )
    )
    due_date = forms.DateTimeField(
        label='Vencimento',
        widget=forms.DateTimeInput(
        )
    )

    class Meta:
        model = ToDoItem
        fields = ('todo_list', 'title', 'description', 'due_date')

class ToDoListForm(forms.ModelForm):

    class Meta:
        model = ToDoList
        fields = ['title', ]
        labels = {
            'title': 'Título',
        }