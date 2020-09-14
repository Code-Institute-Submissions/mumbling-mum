from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import BlogEntry, Category, Comment
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import BlogEntryForm, CategoryForm, CommentForm


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

def blog_list_by_category(request, cat_id):
    """ A view to show blog entries filtered by category """
    blogentries = BlogEntry.objects.filter(category=cat_id)
    categories = Category.objects.all()
    filtered = True
    context = {
        'blogentries': blogentries,
        'categories': categories,
        'cat_id': cat_id,
        'filtered' : filtered,
    }
    template = 'blog/blog_list.html'
    return render(request, template, context)

@login_required
def like_entry(request, blogentry_id):
    """A View to record when the like button has been selected. """
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
    """ A view to show individual blog Entry, Comments and Likes""" 
    blogentry = get_object_or_404(BlogEntry, pk=blogentry_id)
    categories = Category.objects.all()
    comments = Comment.objects.filter(blog_entry=blogentry_id)
    form = CommentForm()
    user = request.user
    liked = False
    if blogentry.likes.filter(id=request.user.id).exists():
        liked = True
    else:
        liked = False
    context = {
        'blogentry' : blogentry,
        'categories': categories,
        'liked': liked,
        'comments': comments,
        'form':form,
        'user':user,
    }
    template_name = 'blog/blog_detail.html'
    return render(request, template_name, context)

@login_required
def add_blog_entry(request):
    """ A view to display the add Blog Entry Form"""
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
def add_comment(request, blogentry_id):
    """ A view to add a comment to a blog post"""
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment=form.save()
            Comment.objects.filter(pk=comment.pk).update(blog_entry=blogentry_id)
            Comment.objects.filter(pk=comment.pk).update(author=user)
            return redirect(reverse('blog_detail', args=[blogentry_id] ))

@login_required
def delete_comment(request, blogentry_id, comment_id):
    """ A view to delete a comment when the delete comment button is pressed """
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect(reverse('blog_detail', args=[blogentry_id] ))

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
def manage_blog_by_category(request, cat_id):
    """ A view to manage blog entries filtered by category """
    user= request.user
    if user.is_staff:
        manage_blog = True
        blogentries = BlogEntry.objects.filter(category=cat_id)
        categories = Category.objects.all()
        filtered = True
        context = {
            'blogentries': blogentries,
            'categories': categories,
            'cat_id': cat_id,
            'filtered' : filtered,
            'manage_blog':manage_blog,
        }
        template = 'blog/blog_list.html'
        return render(request, template, context)

@login_required
def edit_blog_entry(request, blogentry_id):
    """ A View to allow staff member to edit blog entry """
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

@login_required
def manage_categories(request):
    """ A view to add, modify and delete categories """
    user= request.user
    if user.is_staff:
        categories = Category.objects.all()
        template = 'blog/manage_categories.html'
        context = {
            'categories': categories,
        }
        return render(request, template, context)
    else:
        # redirect to home page only Staff can view the manage items page
        return redirect(reverse('home'))

@login_required
def add_category(request):
    """ A view to allow staff to add a new item to the store """
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('manage_categories'))
    else:
        form = CategoryForm()
        context = {
            'form':form,
        }
        template = 'blog/add_category.html'
        return render(request, template, context)

@login_required
def edit_category(request, cat_id):
    """ A view to allow staff to edit a blog category """
    category = get_object_or_404(Category, pk=cat_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST or None, request.FILES or None, instance=category)
        if form.is_valid():
            form.save()
            return redirect(reverse('manage_categories'))

    else:
        form = CategoryForm(instance=category)
        context = {
            'form':form,
            'category' : category,
        }
        return render(request, 'blog/edit_category.html', context)

@login_required
def delete_category(request, cat_id):
    """ Delete a blog category """
    category = get_object_or_404(Category, pk=cat_id)
    category.delete()
    return redirect(reverse('manage_categories'))

