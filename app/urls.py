from django.urls import path
from .views import index, VocalizacionView, intensidad, save_audio, LoginView, registro, vocalizacion, preregistro, buscar_rut, preregistrados


urlpatterns = [
    path('', index, name="index"),
    #path('memorama/', memorama, name="memorama"),
    #path('crucigrama/', crucigrama, name="crucigrama"),
    #path('vocalizacion/', VocalizacionView.as_view(), name="vocalizacion"),
    path('vocalizacion/', vocalizacion, name="vocalizacion"),
    path('save_audio/', save_audio, name="save_audio"),
    path('intensidad/', intensidad, name="intensidad"),
    path('login/', LoginView.as_view(), name="login"),
    path('registro/', registro, name="registro"),
    path('preregistro/', preregistro, name="preregistro"),
    path('preregistrados/', preregistrados, name="preregistrados"),
    path('buscar_rut/', buscar_rut, name="buscar_rut"),
    #path('eva_param_func/', eva_param_func, name="eva_param_func"),
    #path('eva_param_text/', eva_param_text, name="eva_param_text"),
]
