from django.urls import path
from .views import index, VocalizacionView, IntensidadView, save_audio, LoginView, registro


urlpatterns = [
    path('', index, name="index"),
    #path('memorama/', memorama, name="memorama"),
    #path('crucigrama/', crucigrama, name="crucigrama"),
    path('vocalizacion/', VocalizacionView.as_view(), name="vocalizacion"),
    path('save_audio/', save_audio, name="save_audio"),
    path('intensidad/', IntensidadView.as_view(), name="intensidad"),
    path('login/', LoginView.as_view(), name="login"),
    path('registro/', registro, name="registro"),
    #path('medidor/', medidor, name="medidor"),
    #path('eva_param_func/', eva_param_func, name="eva_param_func"),
    #path('eva_param_text/', eva_param_text, name="eva_param_text"),
]
