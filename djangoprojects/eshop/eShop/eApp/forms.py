from django import forms



from .models import products

# class productsforms(forms.Form):
#     Title = forms.CharField(widget=TinyMCE(attrs={'cols':80,'row':30}))


# class Meta:
#     model = FlatPage



class ProductForms(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = products
 
        # specify fields to be used
        fields = [
            "product_id",
            "title",
            "oldprice",
            "newprice",
            "description",
            "specification",
            "reviews",
            "comments",
            "image",
            "productImages"
        ]
        widgets={
            'product_id':forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'oldprice': forms.TextInput(attrs={'class':'form-control'}),
            'newprice': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'specification': forms.TextInput(attrs={'class':'form-control'}),
            'reviews': forms.TextInput(attrs={'class':'form-control'}),
            'comments': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'productImages': forms.FileInput(attrs={'class':'form-control','multiple':True}),
        }



from django import forms
from .models import Post, Images

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    body = forms.CharField(max_length=245, label="Item Description.")
 
    class Meta:
        model = Post
        fields = ('title', 'body', )
 
 
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ('image', )