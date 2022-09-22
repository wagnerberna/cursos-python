from django.http import HttpResponse
from django.shortcuts import redirect, render
from helpdesk.api.viewsets import DemandViewSet
from helpdesk.forms import DemandFormCreate, DemandFormUpdate

demand_view_set = DemandViewSet()

# Create your views here.
def demand(request):
    try:
        all_demands = demand_view_set.get_all()
        # print(all_demands)

        context = {"title": "Demandas", "all_demands": all_demands}

        return render(
            request,
            "helpdesk/pages/demand_main.html",
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise


# envia form importado / None para enviar o mesmo vazio
# valida formulário para salvar
# redireciona para a rota da lista pelo apelido
# Request .post pega o formulário, files as medias
def new_demand(request):
    form = DemandFormCreate(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect("demands_list")

    return render(request, "helpdesk/pages/demand_create.html", {"create_form": form})


# get_object_or_404 tenta recuperar objeto ou retorna 404
def demand_update(request, id):
    demand = demand_view_set.get_by_id(id)
    form = DemandFormUpdate(request.POST)


def about(request):
    return HttpResponse("Sistema TI de Helpdesk")
