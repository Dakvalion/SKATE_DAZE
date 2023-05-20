# SKATE DAZE 🛹

A simple website as university project using django framework ✌

[<img  width="900" height="450" align="center" src="SKATE_DAZE_web/SKATE_DAZE/Items/Items/2023-05-19_22-58-48.png" 
/>](https://www.youtube.com/watch?v=CseQwi-C8vU)

# Backend

## Using forms to register new users
The same technology is used for mailing form ✉
```python
class RegForm(forms.ModelForm):
    class Meta:
        model = Reg
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class': "input", 'placeholder': 'email'}),
            'phone': forms.TextInput(attrs={'class': "input", 'placeholder': 'Телефон'}),
            'name': forms.TextInput(attrs={'class': "input", 'placeholder': 'Имя'}),
            'password1': forms.TextInput(attrs={'class': "input", 'placeholder': 'Пароль'}),
            'password2': forms.TextInput(attrs={'class': "input", 'placeholder': 'Пароль повторно'}),
        }
```

![2023-05-20_00-12-29](https://github.com/Dakvalion/SKATE_DAZE/assets/105875517/b8d74b26-47ab-4f6d-afe2-92299db2e090)

## Navigate between pages using site elements, or ready-made urls
First, do it with views.py
```python
def SD(request):
    error = ''
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "No"

    form = MailForm()
    return render(request, 'main/SD.html', {'title': 'SKATE DAZE', 'form': form, 'error': error})
```
And then, create an url-path to your view
```python
urlpatterns = [
    path('', views.SD),
    path('LogIn', views.LogIn),
    path('SignIn', views.SignIn),
    path('Catalog', views.Catalog),
]
```
## Place your items using Paginator
Do this in views.py
```python
def Catalog(request):
    products = Items.objects.all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    return render(request, 'main/Catalog.html', {'page_obj': page_obj, 'title': 'Каталог', 'products': products})
```
![2023-05-20_00-06-11](https://github.com/Dakvalion/SKATE_DAZE/assets/105875517/5a287bee-a230-498a-93f5-fb2569e57144)

# Frontend

For header and footer using base.html file, which extends with a content of the page <br>
Use static files to add some style for your templates 🎀
```html
{% extends 'main/base.html'%}
{% load static %}

{% block content %}
<section>
	<div class="container">
		<div class="wrapper">
			<div class="mainBill">
				<p class="head2">
					<span>SKATE DAZE -</span><br>
					ПОМОГАЕМ СКЕЙТБОРДИНГУ
					РАЗВИВАТЬСЯ
				</p>
				<img src="{% static 'SD/img/mainLine.png' %}" alt="line1">
				<p class="par1">здесь ты найдёшь все детали для своей доски и не только</p>
				<a href="/Catalog" class="btn">Перейти в каталог</a>
			</div>
			<div>
				<img src="{% static 'SD/img/main.jpg' %}" alt="mainPaint" class="top">
				<img src="{% static 'SD/img/mainRec.png' %}" alt="Rectangle" class="rec">
			</div>
		</div>
	</div>
</section>
```

CSS styles applied in this way ( example on base.html)
```html
<link rel="stylesheet" href="{% static 'SD/css/SD.css' %}? 20230425">
```
