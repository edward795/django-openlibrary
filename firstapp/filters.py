import django_filters
from .models import Book

class BookFilters(django_filters.FilterSet):
    CHOICES=(
        ('ascending','Ascending'),
        ('descending','Descending')
    )

    ordering=django_filters.ChoiceFilter(label='Ordering',choices=CHOICES,method='filter_by_order')
    

    class Meta:
        model=Book
        fields={
            'title':{'icontains'},
            'author':{'icontains'}
        }

    def filter_by_order(self,queryset,name,value):
        expression='title' if value=='ascending' else '-title'
        return queryset.order_by(expression)

    