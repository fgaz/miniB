from django.shortcuts import render
from django.http import HttpResponseRedirect
#models
from board.models import *
#forms
from board.forms import *

posts_per_page = 5


def board(request, pageNumber=None, postNumber=None):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Post(
                title=cd['title'],
                content=cd['content'],
                picURL=cd['picURL'],
            ).save()
            return HttpResponseRedirect('/#lel')
    else:
        form = PostForm()

    totalposts = Post.objects.count()
    totalpages = totalposts//posts_per_page+2

    if postNumber:
        pageNumber = (totalposts-int(postNumber))//posts_per_page+1
        return HttpResponseRedirect('/' + str(pageNumber) + '#' + str(postNumber))

    lastpost = totalposts - (int(pageNumber)-1)*posts_per_page
    firstpost = lastpost - posts_per_page

    posts = Post.objects.filter(id__gte=firstpost, id__lte=lastpost)
    return render(request, 'board.html', {'form': form, 'posts': posts, 'currentPage':pageNumber, 'pages': range(1,totalpages), 'highlightedPost': postNumber, })