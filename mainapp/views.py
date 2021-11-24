from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def products(request):
    return render(request,'products.html')

def main(request):
    title = 'главная'
    
    products = Product.objects.all()[:4]
        
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)
