from django.shortcuts import render

from families.models import Familia
from families.forms import FamiliaForm

def index(request):

    families = Familia.objects.all()

    return render(
        request,
        'families/index.html',
        {
            'families': families
        }
    )

def new_family(request):
    familia_form = FamiliaForm()
    mensaje = ''
    if request.method == 'GET':
        familia_form = FamiliaForm()
    elif request.method == 'POST':
        familia_form = FamiliaForm(data=request.POST)
        if familia_form.is_valid():
            familia_form.save()
            familia_form = FamiliaForm()


    return render(
        request,
        'families/new_family.html',
        {
            'familia_form': familia_form
        }
    )


def family_detail(request, family_id):

    family = Familia.objects.get(pk=family_id)

    return render(
        request,
        'families/detail.html',
        {
            'family': family
        }
    )
# Personas
# Listado
# detalle
# crear nueva 
# editar Personas

# famila
# editar
# formsets
# formsets js