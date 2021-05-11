from django.urls import path,include
from . import views

urlpatterns = [
    path("tbl1/",views.loadtable1,name="tbl1"),
    path("category/",views.viewcategory,name="cate"),
    path("addprod/",views.addproduct,name="addpro"),
    path("addproduct/",views.insertproduct,name="addprod"),
    path("showproduct/",views.showprod,name="showprod"),
    path("editproduct/<int:pk>",views.editproduct,name="editproduct"),
    path("editpro/<int:pk>",views.editpro,name="editprod"),
    path("deleteproduct/<int:pk>",views.deleteproduct,name="delproduct"),
    path("reqpasswrd/",views.reqpasswrd,name="reqpasswrd"),
    path("chngepaswd/",views.changepassword,name="chngepaswd"),
    path("profile/<int:pk>",views.profile,name="profile"),
    path("",views.welcome,name="welcome"),
    path("editprof/<int:pk>",views.editprofile,name="editprofile"),
    path("reportorder/",views.reportorder,name="reportorder"),
    path("reportproduct/",views.reportproduct,name="reportproduct"),
    path("onselect/",views.onselect,name="onselect"),
    path("onc/",views.onc,name="onc"),
]