from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from rest_framework.generics import ListAPIView

from .models import Display
from .models import Slide
from .serializers import SlideSerializer


class DisplayDetail(DetailView):
    model = Display


class DisplayList(ListView):
    model = Display


class DisplayCreate(CreateView):
    model = Display
    fields = ['name', 'description', 'tags']


class DisplayDelete(DeleteView):
    model = Display
    success_url = reverse_lazy('signage:display_list')


class DisplaySlides(ListAPIView):
    serializer_class = SlideSerializer

    def get_queryset(self):
        display = Display.objects.get(pk=self.kwargs['pk'])
        return display.get_slides()


class DisplayUpdate(UpdateView):
    model = Display
    fields = ['name', 'description', 'tags']


class SlideList(ListView):
    model = Slide


class SlideCreate(CreateView):
    model = Slide
    fields = ['name', 'description', 'image', 'start', 'end', 'duration', 'weight', 'tags']


class SlideDelete(DeleteView):
    model = Slide
    success_url = reverse_lazy('signage:slide_list')


class SlideUpdate(UpdateView):
    model = Slide
    fields = ['name', 'description', 'image', 'start', 'end', 'duration', 'weight', 'tags']
