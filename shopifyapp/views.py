from django.shortcuts import render , redirect
from django.views import View
from shopifyapp.models import Category, Product 
from django.db.models import Q


class IndexPageView(View):
    def get(self, request):
        products = Product.objects.exclude(image='').order_by('-id')[:3]

        return render (request, 'shopifyapp/index.html', context={'products' : products})
    
class CreateProductView(View):
    flag = False
    def get(self, request):
        all_category = Category.objects.all()
        return render (request, 'shopifyapp/add-product.html', {'category' : all_category })
    
    def post(self, request) :
        flag = False
        try :
            category_id = request.POST.get('category')
            obj = Category.objects.get(pk=category_id)



            original_price_user = eval (request.POST.get("oprice") )
            discount_percentage_user = eval (request.POST.get("dprice"))
            discount_price = original_price_user * discount_percentage_user / 100
            selling_price = original_price_user - discount_price

            Product.objects.create(
                name = request.POST.get("pname") ,
                discription = request.POST.get("discription") ,
                original_price = original_price_user ,
                discount_percentage = discount_percentage_user ,
                selling_price = selling_price ,
                image = request.FILES.get("image") ,
                category = obj , 
            )
            return redirect('shopify:home')
        except Exception as e :
            flag = False
            print(f'{type (e)._name_} : {e}')

        return render(request , 'shopifyapp/add-product.html' , {'flag' : flag})
    
class CreateCategoryView(View):
    flag = False 
    def get(self, request) :
        return render(request , 'shopifyapp/add-category.html')
    
    def post(self, request) :
        flag = False
        try :
            category_name = request.POST.get('cname')
            category = Category(name=category_name)
            category.save()

            print("Product Added success")
            flag = True
            return redirect('shopify:home')
        except Exception as e :
            flag = False
            print(f'{type (e)._name_} : {e}')

        return render(request , 'shopifyapp/add-category.html' , {'flag' : flag})
    
    
class ViewProduct(View):

    def get(self, request , id):
        print(id)
        product = Product.objects.get(pk=id)
        return render(request , 'shopifyapp/view-product.html',{"product":product})
     
class EditProduct(View):

    def get(self, request , id):
        product = Product.objects.get(pk=id)
        return render(request , 'shopifyapp/edit-product.html',{"product":product})
    
    def post(self, request,id):
        try:
            db_product = Product.objects.get(pk=id)

            original_price_user = eval(request.POST.get("oprice"))
            discount_percentage_user = eval(request.POST.get("dprice"))
            discount_price = original_price_user * discount_percentage_user / 100
            selling_price = original_price_user - discount_price

            db_product.name = request.POST.get("pname")
            db_product.discription = request.POST.get("discription")
            db_product.original_price = original_price_user
            db_product.discount_percentage = discount_percentage_user
            db_product.selling_price = selling_price

            if request.FILES.get("image"):
                db_product.image = request.FILES.get("image")

            db_product.save()
            print("Product updated successfully")
            return redirect('shopify:home')
        except Exception as e:
            print(f'{type(e)._name_} : {e}')
        return render(request, 'shopifyapp/add-product.html')



class DeleteProduct(View):
    def get(self, request , id):
        product = Product.objects.get(pk=id)
        product.delete()
        return redirect('shopify:home')
    
    
class SearchProduct(View):
    def post(self , request):

        search = request.POST.get("search")

        search_list = Product.objects.filter(Q(name__icontains=search) | Q(category__name__icontains=search))

        print( search_list )

        return render(request ,"shopifyapp/searchlist.html" , {'search_list' : search_list} )