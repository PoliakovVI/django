from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('preparation', views.preparation, name="preparation"),
    path('stage1', views.stage_one, name="stage1"),
    path('stage2', views.stage_two, name="stage2"),
    path('stage3', views.stage_three, name="stage3"),
    path('accept_<int:req_id>', views.accept, name="accept"),
    path('reject_<int:req_id>', views.reject, name="reject"),
    path('account', views.account, name="account"),
    path('login', views.log_in, name="login"),
    path('logout', views.log_out, name="logout"),
    path('records', views.records, name="records"),
    path('record_<int:note_id>', views.record_and_comments, name="record"),
    path('signup', views.sign_up, name="signup"),
    path('request', views.record_request, name="request"),
]
