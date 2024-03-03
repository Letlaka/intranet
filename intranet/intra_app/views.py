from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Document


# Create your views here.
def index(request):
    context = {"title": "Home"}
    return render(request, "intra_app/index.html", context)

def ict(request):
    policies = Document.objects.all().order_by("ref_number")
    
    per_page = 5
    page_number = request.GET.get('page',1)
    paginator = Paginator(policies, per_page)
    page_obj = paginator.get_page(page_number)

    context = {
        "title": "ICT Policies",
        "policies": policies,
        "paginator": paginator,
    }
    return render(request, "intra_app/ict.html", context)


def hr(request):
    return render(request, "intra_app/hr.html", {"title": "HR Policies"})

def error404(request):
    context = {"title": "404"}
    return render(request, "intra_app/404.html", context)