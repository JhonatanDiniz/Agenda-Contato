from django.shortcuts import redirect, render, get_object_or_404
from contact.models import Contact
from django.db.models import Q

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    context ={
        'contacts': contacts
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):
    result_search = request.GET.get('q', '').strip()
    
    if result_search == '':
        return redirect('contact:index')
    
    contacts = Contact.objects \
        .filter(show=True)\
        .filter(Q(first_name__icontains=result_search) | 
                Q(last_name__icontains=result_search) | 
                Q(email__icontains=result_search) | 
                Q(phone__icontains=result_search)
        ).order_by('-id')
    context ={
        'contacts': contacts
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact.objects, pk=contact_id, show=True)

    context = {
        'contacts': single_contact
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
