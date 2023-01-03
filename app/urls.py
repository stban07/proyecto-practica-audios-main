from django.urls import path
from .views import index, crucigrama, eva_param_func, eva_param_text, memorama, VocalizacionView, IntensidadView, medidor


urlpatterns = [
    path('', index, name="index"),
    #path('memorama/', memorama, name="memorama"),
    #path('crucigrama/', crucigrama, name="crucigrama"),
    path('vocalizacion/', VocalizacionView.as_view(), name="vocalizacion"),
    #path('intensidad/', intensidad, name="intensidad"),
    path('intensidad/', IntensidadView.as_view(), name="intensidad"),
    #path('medidor/', medidor, name="medidor"),
    #path('eva_param_func/', eva_param_func, name="eva_param_func"),
    #path('eva_param_text/', eva_param_text, name="eva_param_text"),
]
