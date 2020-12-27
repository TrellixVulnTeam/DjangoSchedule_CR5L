from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 3)
    page = request.GET.get('p')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/index.html', {
        'contacts' : contacts
    })


def view_contact(request, contact_id):
    #contact = Contact.objects.get(id=contact_id)
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts/view_contact.html', {
          'contact' : contact
    })