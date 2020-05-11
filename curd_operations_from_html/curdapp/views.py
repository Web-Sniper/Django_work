from django.shortcuts import render
from .models import CurdOperations
from .forms import AddProduct,UpdateProduct,DeleteProduct
from django.http.response import HttpResponse
def index_view(request):
    return render(request,'index.html')
def addprod_view(request):
    if request.method=="POST":
        add = AddProduct(request.POST)
        if add.is_valid():
            prod_name = request.POST.get('prod_name')
            prod_id = request.POST.get('prod_id')
            prod_cost = request.POST.get('prod_cost')
            prod_color = request.POST.get('prod_color')
            prod_weight = request.POST.get('prod_weight')
            data = CurdOperations(
                prod_name=prod_name,
                prod_id=prod_id,
                prod_cost=prod_cost,
                prod_color=prod_color,
                prod_weight=prod_weight
            )
            data.save()
            add = AddProduct()
            res = "<script>alert('Product Add Successfully')</script>"
            return render(request,'add_prod.html',{'add':add,'res':res})
        else:
            return HttpResponse("Invalid User Data")
    else:
        add = AddProduct()
        return render(request, 'add_prod.html', {'add': add})
def updateprod_view(request):
    if request.method=="POST":
        update = UpdateProduct(request.POST)
        if update.is_valid():
            prod_id = request.POST.get('prod_id')
            prod_cost = request.POST.get('prod_cost')
            prod = CurdOperations.objects.filter(prod_id=prod_id)
            if prod:
                prod.update(prod_cost=prod_cost)
                update = UpdateProduct()

                return render(request,'update_prod.html',{'update':update})
            else:
                return HttpResponse("Can't Found Product....Please Enter Valid ID")
        else:
            return HttpResponse("Invalid User Data")
    else:
        update = UpdateProduct()
        return render(request, 'update_prod.html', {'update': update})
def deleteprod_view(request):
    if request.method=="POST":
        deletepro = DeleteProduct(request.POST)
        if deletepro.is_valid():
            prod_id = request.POST.get('prod_id')
            item = CurdOperations.objects.filter(prod_id=prod_id)
            if item:
                item.delete()
                deletepro = DeleteProduct()
                return render(request,'delete_prod.html',{'deletepro':deletepro})
            else:
                return HttpResponse("Product ID didn't match please enter correct ID...")
        else:
            return HttpResponse("Invalid User Data")
    else:
        deletepro = DeleteProduct()
        return render(request, 'delete_prod.html', {'deletepro': deletepro})
def retriveprod_view(request):
    product = CurdOperations.objects.all()
    return render(request,'products.html',{'product':product})
