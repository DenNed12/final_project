from django_filters import FilterSet
from .models import Post
from django_filters import FilterSet,ModelChoiceFilter,DateTimeFilter, ChoiceFilter
from django.forms import DateTimeInput
class PostFilter(FilterSet):
    category = ModelChoiceFilter(field_name='postCategory',
                                 queryset= 'Post.objects.get(postCategory)',
                                 label='Category',
                                 empty_label='Select a category'),
    added_after = DateTimeFilter(
        field_name='added_at',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains']
        }