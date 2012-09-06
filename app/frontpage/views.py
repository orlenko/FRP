from django.shortcuts import render

def front_page_view(request, *args, **kwargs):
    # Generic render view
    ret = dict()
    return render(request, 'frontpage/frontpage.html', ret)

