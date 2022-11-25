from django.shortcuts import render
from mango.models import post
def index(request):
     allpost=post.objects.all()
     context={'allpost':allpost}
     return render(request, 'index.html',context)
# Create your views here.
