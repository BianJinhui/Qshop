from django.urls import path,re_path
from Seller.views import *

urlpatterns = [
    re_path('^$', index),
    path('index/', index),
    path('login/', login),
    path('logout/', logout),
    path('goods_add/', goods_add, name = "goods_add"),
    path('goods_list/', goods_list, name = "goods_list"),
    re_path('goods_change/(?P<id>\d+)/', goods_change, name="goods_change"),
    re_path('goods_del/(?P<id>\d+)/', goods_del, name="goods_del"),
    path('goodsType_add/',goodsType_add, name="goodsType_add"),
    re_path('goodsType_change/(?P<id>\d+)/', goodsType_change, name="goodsType_change"),
    re_path('goodsType_del/(?P<id>\d+)/', goodsType_del, name="goodsType_del"),
    path('tList/', goodsType_list, name="goodsType_list"),
    path('example/', example),
]
