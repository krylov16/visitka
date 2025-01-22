from django import forms

class QuestForm(forms.Form):
    name = forms.CharField(label="Имя")
    email = forms.EmailField(label="E-mail")
    question = forms.CharField(label="Вопрос", widget=forms.Textarea)