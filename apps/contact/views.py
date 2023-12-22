from django.shortcuts import render, redirect

from contact.forms import ContactForm


# Create your views here.


def contactView(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/contact/')

    ctx = {'form': form}
    return render(request, 'contact_template/contact.html', ctx)
