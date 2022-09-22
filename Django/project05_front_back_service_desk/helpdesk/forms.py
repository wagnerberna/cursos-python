from django.forms import ModelForm

from .models import Demand


# importa model para criar o formulário
class DemandFormCreate(ModelForm):
    class Meta:
        model = Demand
        fields = ["user_name", "category", "description", "image"]


class DemandFormUpdate(ModelForm):
    class Meta:
        model = Demand
        fields = [
            "user_name",
            "category",
            "description",
            "image",
            "attendant",
            "status",
            "solution",
        ]
