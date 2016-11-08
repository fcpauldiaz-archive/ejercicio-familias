from django.shortcuts import render

from families.models import Persona, Familia
from families.forms import FamiliaForm, PersonaForm
from django.forms import formset_factory

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

def list_people(request):
    people = Persona.objects.all()

    return render(
        request,
        'families/list_people.html',
        {
            'people': people
        }
    )


def new_person(request):
    message = ''
    if request.method == 'GET':
        person_form = PersonaForm()

    elif request.method == 'POST':
        person_form = PersonaForm(request.POST)
        message = "Persona exitosamente guardada"
        if person_form.is_valid():
            person_form.save()
            person_form = PersonaForm()

    else:
        pass

    return render(
        request,
        'families/new_person.html',
        {
            'person_form': person_form,
            'message': message
        }
    )


def edit_persona(request, persona_id):
    persona = Persona.objects.get(pk=persona_id)
    message = ''
    if request.method == 'GET':
        person_form = PersonaForm(instance=persona)

    elif request.method == 'POST':
        person_form = PersonaForm(request.POST)
        message = "Persona exitosamente guardada"
        if person_form.is_valid():
            person_form.save()
            person_form = PersonaForm()

    else:
        pass

    return render(
        request,
        'families/person_edit.html',
        {
            'person_form': person_form,
            'message': message
        }
    )
def formset_familia(request):
    FamiliaFormSet = formset_factory(FamiliaForm, extra=5)
    message = ''
    if request.method == 'GET':
        familia_formset = FamiliaFormSet()
    elif request.method == 'POST':
        familia_formset = FamiliaFormSet(request.POST)
        for form in familia_formset:
            if form.is_valid():
                form.save()
        familia_formset = FamiliaFormSet()
        message = 'Se ha guardado exitosamente'

  
    
    return render(
        request,
        'families/familia_formset.html',
        {
            'formset': familia_formset,
            'message': message
        }
    )

def formset_persona(request):
    PersonFormSet = formset_factory(PersonaForm, extra=5)
    message = ''
    if request.method == 'GET':
        persona_formset = PersonFormSet()
    elif request.method == 'POST':
        persona_formset = PersonFormSet(request.POST)
        for form in persona_formset:
            if form.is_valid():
                form.save()
        persona_formset = PersonFormSet()
        message = 'Se ha guardado exitosamente'

    return render(
        request,
        'families/persona_formset.html',
        {
            'formset': persona_formset,
            'message': message
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