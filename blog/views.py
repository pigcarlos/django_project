import imp
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import View


# My views here.

class Bloglistview(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request,'blog_list.html', context,),
