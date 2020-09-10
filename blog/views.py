from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import BlogEntry, Category, Comment


def blog_list(request):
    """ A view to show all Blog Entries """
    blogentries = BlogEntry.objects.all()
    categories = Category.objects.all()
    comments = Comment.objects.all()
    context = {
        'blogentries': blogentries,
        'categories': categories,
    }
    template_name = 'blog/blog_list.html'
    return render(request, template_name, context)

def like_entry(request, blogentry_id):
    blogentry= get_object_or_404(BlogEntry, pk=blogentry_id)
    blogentry.likes.add(request.user)
    return redirect(reverse('blog_list'))


def blog_detail(request, blogentry_id):
    """ A view to show individual item details """ 
    blogentry = get_object_or_404(BlogEntry, pk=blogentry_id)
    categories = Category.objects.all()
    context = {
        'blogentry' : blogentry,
        'categories': categories,
    }
    template_name = 'blog/blog_detail.html'
    return render(request, template_name, context)
