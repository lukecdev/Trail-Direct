from django.shortcuts import render
from .forms import NewsletterForm

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def Newsletter(request):
    """
    A view for users to subscribe to the site's newsletter
    """
    form = NewsletterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thanks for subscribing to our newsletter!'
                )
            return redirect('home')
        messages.error(request, 'An error has occurred. Please try again.')
    template = 'home/newsletter.html'
    context = {
        'form': form,
    }
    return render(request, template, context)