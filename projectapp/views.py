from django.http import JsonResponse
from django.shortcuts import render,redirect

from projectapp.models import Branches

from .forms import MyForm
# Create your views here.

def demo(request):
    obj=Branches.objects.all()
    return render(request,"index.html",{'result':obj})

def branch(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process form data (e.g., save to database)
            # Redirect to some page after successful form submission
            return render(request, 'submit.html')
    else:
        form = MyForm()
    return render(request, 'branches.html', {'form': form})
# def get_branches(request):
#     district = request.GET.get('district')
#     # Here you would fetch branches based on the selected district
#     # For demonstration, I'm just returning some hardcoded data
#     if district == 'ernakulam':
#         branches = {'Aluva': 'aluva', 'Edapally': 'edapally'}
#     elif district == 'thrissur':
#         branches = {'Branch 3': 'branch3', 'Branch 4': 'branch4'}
#     else:
#         branches = {}
#     return JsonResponse(branches)



