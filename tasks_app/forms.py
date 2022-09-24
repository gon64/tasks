from django import forms


class createTask(forms.Form):
    title = forms.CharField(label="Título", max_length=200)
    description = forms.CharField(label="Descripción", widget=forms.Textarea)


class createProject(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200)
