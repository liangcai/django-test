from django.views.generic import ListView
from .models import Publisher

# Create your views here.


class PublisherListView(ListView):
    model = Publisher
