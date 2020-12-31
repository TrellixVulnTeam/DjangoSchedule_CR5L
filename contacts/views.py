from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contact
'''Libraries for complexes queries.'''
from django.db.models import Q, Value
from django.db.models.functions import Concat
# MESSAGES LIBRARIES
from django.contrib import messages

# Create your views here.

def index(request):
    contacts = Contact.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contacts, 3)
    page = request.GET.get('p')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/index.html', {
        'contacts' : contacts
    })


def view_contact(request, contact_id):
    #contact = Contact.objects.get(id=contact_id)
    contact = get_object_or_404(Contact, id=contact_id)
    if not contact.mostrar:
        raise Http404()
    return render(request, 'contacts/view_contact.html', {
          'contact' : contact
    })


def search(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        ''' Show messages for cases in what the search bar stay empty or others errors.
        '''
        messages.add_message(
            request,
            messages.ERROR,
            'Field search cannot stay empty.'
        )
        return redirect('index')
    campos = Concat('nome', Value('') ,'sobrenome')
    contacts = Contact.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    paginator = Paginator(contacts, 3)
    page = request.GET.get('p')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/search.html', {
        'contacts': contacts
    })