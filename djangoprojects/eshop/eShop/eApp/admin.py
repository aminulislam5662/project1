from django.contrib import admin

from eApp.models import products 

from .models import *

# Register your models here.

class addproduct(admin.ModelAdmin):
    list_display=('product_id','title','oldprice','newprice','description','specification','reviews','comments','image')





 
# class PostImageAdmin(admin.StackedInline):
#     model = PostImage
 
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImageAdmin]
 
#     class Meta:
#        model = Post
 
# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass

admin.site.register(products,addproduct)
admin.site.register([Post,Images])


# admin.site.register(bags)
# admin.site.register(buyers)

admin.site.register([Interests,City,Mobile,Person,PersonAddress,ProductImages])