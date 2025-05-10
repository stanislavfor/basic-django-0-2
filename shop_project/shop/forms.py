
# from django import forms
from .models import Order
from .models import Product
# from .models import Profile
from django.contrib.auth.models import User
from django import forms
from .models import Profile



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name', 'description', 'price', 'quantity']



class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


# Login
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address_city']  # Список полей в форме



class ClientForm(forms.Form):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Телефон', max_length=15)
    address_city = forms.CharField(label='Город', max_length=100)

    def save(self):
        cleaned_data = self.cleaned_data
        user = User.objects.create_user(
            username=cleaned_data['email'],
            first_name=cleaned_data['first_name'],
            last_name=cleaned_data['last_name'],
            email=cleaned_data['email'],
            password=None  # Пароль не обязателен (для примера)
        )
        Profile.objects.create(
            user=user,
            phone_number=cleaned_data['phone_number'],
            address_city=cleaned_data['address_city']
        )
        return user