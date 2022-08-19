from rest_framework import viewsets, mixins, serializers
from adoptions.models import Animal, Photo, Contact

from django_filters import FilterSet
import django_filters
from django_filters import rest_framework as filters
from django.views import generic

# Create your views here.
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Photo
        fields="__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields="__all__"

class AnimalSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    contacts = ContactSerializer(many=True)
    class Meta:
        model=Animal
        fields="__all__"

class CharInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass

class AnimalFilterSet(FilterSet):
    spice = CharInFilter(lookup_expr='in')
    size = CharInFilter(lookup_expr='in')
    age_gte = django_filters.NumberFilter(field_name="age", lookup_expr='gte')
    age_lte = django_filters.NumberFilter(field_name="age", lookup_expr='lte')
    sex = CharInFilter(lookup_expr='in')



class AdoptionsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AnimalFilterSet

class AnimalDetailView(generic.DetailView):
    model = Animal
    template_name = 'animal.html'
