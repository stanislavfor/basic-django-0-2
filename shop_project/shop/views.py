
from .models import Order
from .forms import OrderForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm
from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.views.generic.edit import FormView
from .forms import ClientProfileForm
from .models import Profile
from .models import OrderItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import ProfileForm
from django.shortcuts import get_object_or_404
from .forms import ClientForm




# Представление для главной страницы (/)
def home_page(request):

    return render(request, 'index.html')

# Order - Представление для добавления нового заказа
class AddOrder(CreateView):
    model = Order
    template_name = 'add_order.html'
    success_url = '/'
    form_class = OrderForm

# Order - Представление для редактирования заказа
class EditOrder(UpdateView):
    model = Order
    template_name = 'edit_order.html'
    success_url = '/'
    form_class = OrderForm

def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders_list')  # перенаправляем на страницу со списком заказов
    else:
        form = OrderForm(instance=order)
    return render(request, 'update_order.html', {'form': form, 'order': order})

# Order - Представление для удаления заказа
class DeleteOrder(DeleteView):
    model = Order
    success_url = '/'

# Product - Представление для добавления нового продукта
class AddProduct(CreateView):
    model = Product
    template_name = 'add_product.html'
    success_url = '/'
    form_class = ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')  # Перенаправление на страницу со списком товаров
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

# Product - Представление для редактирования продукта
class EditProduct(UpdateView):
    model = Product
    template_name = 'edit_product.html'
    success_url = '/'
    form_class = ProductForm

# Product - Представление для удаления продукта
class DeleteProduct(DeleteView):
    model = Product
    success_url = '/'

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products_list')  # перенаправляем на страницу со списком товаров
    return render(request, 'delete_product.html', {'product': product})

# Client - Обновление профиля текущего пользователя

@login_required
def update_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    if request.method == 'POST':
        form = ClientProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(reverse('home'))
    else:
        form = ClientProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})


# Client - Добавление профиля нового пользователя

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients_list') 
    else:
        form = ClientForm()
    return render(request, 'add_client.html', {'form': form})


# Login

@login_required(login_url='/accounts/login/')
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form': form})


@login_required(login_url='/accounts/login/')
def update_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})


# Отдельные страницы

def clients_list(request):
    clients = Profile.objects.all()
    context = {'clients': clients}
    return render(request, 'clients_list.html', context)

def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)

def products_total(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_total.html', context)

def orders_list(request):
    orders = Order.objects.select_related('client').all()
    context = {'orders': orders}
    return render(request, 'orders_list.html', context)

def client_detail(request, client_id):
    client = get_object_or_404(Profile, id=client_id)
    return render(request, 'client_detail.html', {'client': client})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'order_detail.html', {'order': order, 'order_items': order_items})

