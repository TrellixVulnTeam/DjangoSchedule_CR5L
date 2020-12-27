from django.shortcuts import render
from .models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/index.html', {
        'contacts' : contacts
    })


def view_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'contacts/view_contact.html', {
        'contact' : contact
    })