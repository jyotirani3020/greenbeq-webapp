from django import forms
from .models import Post, BlogCategory

choices = BlogCategory.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title', 'blog_category', 'text', 'blog_image')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'blog_category':forms.Select(choices = choice_list, attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),
            'blog_image':forms.FileInput(attrs={'class':'form-control'}),
            

        }
