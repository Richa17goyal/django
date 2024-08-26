from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'rsProj/all_chai.html', {'chais' : chais})

# apn jb button pe click krenge to vo chai_detail page pe aa ajega

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'rsProj/chai_detail.html', {'chai':chai})

def chai_store_view(request):
    return render(request, 'rsProj/chai_stores.html')

