from django.contrib import admin
from shopifyapp.models import Product, Category

#@admin.register(Product)
#class ProductAdmin(admin.ModelAdmin):
    #exclude = ('name' , 'discription')

#@admin.register(Product)
#class ProductAdmin(admin.ModelAdmin):
    #fields = ('name' , 'discription')

#@admin.register(Product)
#class ProductAdmin(admin.ModelAdmin):
 #   list_display = ('name' , 'discription' , 'image')



admin.site.register(Product)
admin.site.register(Category)
