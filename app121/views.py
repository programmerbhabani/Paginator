from django.shortcuts import render
from .models import StudentModel
from django.core.paginator import Paginator
# Create your views here.
def showindex(request):
    # details=StudentModel.objects.all()
    # return render(request, 'Index.html', {'data': details})
    details = StudentModel.objects.all()
    pa=Paginator(details,3)
    page_no=request.GET.get('page_no',1)
    page=pa.page(page_no)
    return render(request,'Index.html',{'page':page})
