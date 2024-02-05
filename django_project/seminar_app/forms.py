from django import forms
from .models import Author 
import datetime

# Доработаем задачу про броски монеты, игральной кости и случайного числа. 
# Создайте форму, которая предлагает выбрать: монета, кости, числа. 
# Второе поле предлагает указать количество попыток от 1 до 64.

class GameTypeForm(forms.Form):
    game_type = forms.ChoiceField(choices=[('C', 'coins'),('D', 'dice'),('N', 'number')])
    throws_number = forms.IntegerField(min_value=1, max_value=64)

# Продолжаем работу с авторами, статьями и комментариями. 
# Создайте форму для добавления нового автора в базу данных. 
# Используйте ранее созданную модель Author
    
# class AuthorAddForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     bio = forms.CharField()
#     birthday = forms.DateField(initial=datetime.date.today) 

# второй вариант формы:
class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'last_name', 'email', 'bio', 'birthday'] 

# Аналогично автору создайте форму добавления новой статьи. 
# Автор статьи должен выбираться из списка (все доступные в базе данных авторы).
        
class PostAddFormWidget(forms.Form):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'class' : 'form-control',
                                                          'placeholder': 'Введите заголовок статьи'}))
    content = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class' : 'form-control',
                                                          'placeholder': 'Введите текст статьи'}))
    publish_date = forms.DateTimeField(initial=datetime.date.today,
                                       widget=forms.DateInput(attrs={'class' : 'form-control',
                                                                     'type' : 'date'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all())   #обращение формы к БД
    category = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class' : 'form-control',
                                                          'placeholder': 'Введите категориюи'}))
    is_published = forms.BooleanField(required=False,
                                      widget=forms.CheckboxInput(attrs={'class' : 'form-chek-input'}))