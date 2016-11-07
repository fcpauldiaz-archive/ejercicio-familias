from django.conf.urls import url
from families import views as families_views

urlpatterns = [
    url(
        r'^$',
        families_views.index,
        name='families_index'),
    url(
        r'^(?P<family_id>[0-9]+)/$',
        families_views.family_detail,
        name='families_family_detail'),
    url(
        r'^new/$',
        families_views.new_family,
        name='families_new'),
     url(
        r'^new_formset/$',
        families_views.formset_familia,
        name='families_new_formset'),
    url(
        r'^list_people/$',
        families_views.list_people,
        name='families_list_people'),
    url(
        r'^new_person/$',
        families_views.new_person,
        name='families_new_person'),
    url(
        r'^person_formset/$',
        families_views.formset_person,
        name="families_new_person_formset"
    ),
    url(
        r'^(?P<persona_id>[0-9]+)/edit_person/$',
        families_views.edit_person,
        name='families_edit_person'),
]
