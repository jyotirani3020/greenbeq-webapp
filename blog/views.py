from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView,CreateView, UpdateView,DeleteView)
from .models import Post, BlogCategory
from django.utils import timezone
from .forms import PostForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.
# def home(request):
#     return render(request, "home.html", {})

class HomeView(ListView):
    model = Post    
    template_name = "home.html"

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    def get_context_data(self, *args, **kwargs):
        bcat_menu = BlogCategory.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["bcat_menu"] = bcat_menu
        return context
        

class PostDetailView(DetailView):
    model = Post
    template_name = "post-single.html"

    def get_context_data(self, *args, **kwargs):
        bcat_menu = BlogCategory.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        
        get_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = get_post.total_likes()
        
        context["bcat_menu"] = bcat_menu
        context["total_likes"] = total_likes
        return context
    

class AddPostView(CreateView):
    
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = '__all__'

class AddCategoryView(CreateView):
    
    model = BlogCategory
    
    template_name = "add_category.html"
    fields = '__all__'

class PostUpdateView(UpdateView):
    
    template_name = "update_post.html"
    form_class = PostForm
    model = Post

class PostDeleteView(DeleteView):
   
    model = Post
    success_url = reverse_lazy('home')
    template_name = "delete_post.html"

def BlogCategoryView(request, bcats):

    bcat_menu = BlogCategory.objects.all()
    blog_category_posts = Post.objects.filter(blog_category = bcats.replace('-',' '))
    return render(request, 'blog_category.html', {'bcats': bcats.title().replace('-',' '), 'blog_category_posts':blog_category_posts, 'bcat_menu':bcat_menu})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))



