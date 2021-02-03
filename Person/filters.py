import django_filters
from .models import Personal

class PersonFilter(django_filters.FilterSet):
    # fName = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Personal
        fields = ['codeEmploey', 'nameArabic', 'nameEnglish', 'management', 'jop']
        
