from django.urls import path, re_path, include
from . import views
from django.views.static import serve
from myfiles import settings

urlpatterns = [
    #path('', views.index),
    re_path(r'^del', views.delete),
    re_path(r'^(?P<path>.+\.jpg)', serve, {"document_root":settings.REPO_ROOT}),
    re_path(r'^(?P<path>.+\.jpeg)', serve, {"document_root":settings.REPO_ROOT}),
    re_path(r'^(?P<path>.+\.gif)', serve, {"document_root":settings.REPO_ROOT}),
    re_path(r'^(?P<path>.+\.png)', serve, {"document_root":settings.REPO_ROOT}),
    re_path(r'^(?P<path>.+\.pdf)', serve, {"document_root":settings.REPO_ROOT}),
    re_path(r'^(?P<path>.+\.mp4)', serve, {"document_root":settings.REPO_ROOT}),
    re_path(r'^(.*)$', views.deep),


]


