from django.shortcuts import render
from django.http import HttpResponse
from RNG.webhose_search import run_query

def index(request):
    context_dict={}
    return render(request, 'RNG/index.html', context=context_dict)

def search(request):
    result_list=[]
    query=None
    if request.method == 'POST':
        query=request.POST['query'].strip()
        if query:
            #runs webhose search function
            result_list = run_query(query)
    return render(request,'RNG/search.html',{'result_list':result_list,'search_query':query})
