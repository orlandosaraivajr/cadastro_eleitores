from django.shortcuts import render
from .forms import EleitorForm, EleitorRedeSocialForm
from .models import EleitorModel, EleitorRedeSocialModel


def index(request):
    contexto = {'form_eleitor': EleitorForm(),
                'form_rede_social': EleitorRedeSocialForm()}
    return render(request, 'index.html', contexto)


def cadastro(request):
    if request.method == 'POST':
        form_eleitor = EleitorForm(request.POST)
        form_rede_social = EleitorRedeSocialForm(request.POST)
        if form_eleitor.is_valid() and form_rede_social.is_valid():
            eleitor = EleitorModel.objects.create(**form_eleitor.cleaned_data)
            EleitorRedeSocialModel.objects.create(
                eleitor=eleitor,
                **form_rede_social.cleaned_data)
            return render(request, "index.html")
        else:
            contexto = {'form_eleitor': form_eleitor,
                        'form_rede_social': form_rede_social}
            return render(request, "cadastro.html", contexto)
    else:
        contexto = {'form_eleitor': EleitorForm(),
                    'form_rede_social': EleitorRedeSocialForm()}
        return render(request, "cadastro.html", contexto)


def listar(request):
    pass
