from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import BlogEntry, Category, Comment
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import BlogEntryForm


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

@login_required
def like_entry(request, blogentry_id):
    blogentry= get_object_or_404(BlogEntry, pk=blogentry_id)
    liked = False
    if blogentry.likes.filter(id=request.user.id).exists():
        blogentry.likes.remove(request.user)
        liked = False
    else:
        blogentry.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('blog_detail', args=[str(blogentry_id)]))


def blog_detail(request, blogentry_id):
    """ A view to show individual item details """ 
    blogentry = get_object_or_404(BlogEntry, pk=blogentry_id)
    categories = Category.objects.all()
    liked = False
    if blogentry.likes.filter(id=request.user.id).exists():
        liked = True
    else:
        liked = False
    context = {
        'blogentry' : blogentry,
        'categories': categories,
        'liked': liked
    }
    template_name = 'blog/blog_detail.html'
    return render(request, template_name, context)

@login_required
def add_blog_entry(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = BlogEntryForm(request.POST, request.FILES)
            if form.is_valid():
                blogentry=form.save()
                BlogEntry.objects.filter(pk=blogentry.pk).update(author=user)
                return redirect(reverse('blog_detail', args=[blogentry.pk] ))
        else:
            form = BlogEntryForm()
            context = {
                'form':form,
            }
            template = 'blog/add_blog_entry.html'
            return render(request, template, context)
    else:
        return render(reverse('blog_list'))

@login_required
def manage_blog(request):
    """ View to display All Blog Posts and management actions """ 
    user= request.user
    if user.is_staff:
        manage_blog = True
        blogentries = BlogEntry.objects.all()
        categories = Category.objects.all()
        comments = Comment.objects.all()
        template = 'blog/blog_list.html'
        context = {
            'blogentries': blogentries,
            'categories': categories,
            'manage_blog':manage_blog,
        }
        return render(request, template, context)
    else:
        # redirect to home page only Staff can view tha manage blog page
        return redirect(reverse('home'))

@login_required
def edit_blog_entry(request, blogentry_id):
    """ A View to allow staff member to edit blog entries """
    blogentry = get_object_or_404(BlogEntry, pk=blogentry_id)
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = BlogEntryForm(request.POST or None, request.FILES or None, instance=blogentry)
            if form.is_valid():
                blogentry=form.save()
                BlogEntry.objects.filter(pk=blogentry.pk).update(author=user)
                return redirect(reverse('manage_blog'))
        else:
            form = BlogEntryForm(instance=blogentry)
            context = {
                'form':form,
                'blogentry': blogentry,
            }
            template = 'blog/edit_blog_entry.html'
            return render(request, template, context)
    else:
        return render(reverse('blog_list'))

@login_required
def delete_blog_entry(request, blogentry_id):
    """ Delete a blog entry """
    blogentry = get_object_or_404(BlogEntry, pk=blogentry_id)
    blogentry.delete()
    return redirect(reverse('manage_blog'))
