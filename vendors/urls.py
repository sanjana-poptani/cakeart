from django.urls import path,include
from . import views
from cakeart import models

urlpatterns = [
    path("",views.loadtbl,name="table"),
    path("table2/",views.loadtbl2,name="table2"),
    path("table3/",views.loadtbl3,name="table3"),
    path("table4/",views.loadtbl4,name="table4"),
    path("editdetails/<int:pk>",views.EditPage,name="editpage"),
    path("delpg/<int:pk>",views.delPage,name="delpg"),
    path("deletepg/<int:pk>",views.deletePage,name="deletepg"),
    path("editusr/<int:pk>",views.EditUser,name="edituser"),
    path("editcategory/<int:pk>",views.EditCategory,name="editcategory"),
    path("table3/delcategory/<int:pk>",views.delCategory,name="delcategory"),
    path("editcat/<int:pk>",views.editcat,name="Category"),
    path("addcat/",views.addcat,name="addcat"),
    path("addcategory/",views.AddCategory,name="addcategory"),
    path("editpack/<int:pk>",views.EditPackage,name="editpackage"),
    path("delpack/<int:pk>",views.delPackage,name="delpackage"),
    path("editpackage/<int:pk>",views.EditPack,name="editp"),
    path("addpack/",views.AddPack,name="addpack"),
    path("AddPackage/",views.AddPackage,name="addpackage"),
    path("showproduct/",views.showprod,name="showproduct11"),
    path("addtocart",views.addtocart,name="addtocart"),
    path("cartlist/",views.cartlist,name="cartlist"),
    path("deletecartobj/<int:pk>",views.deletecartobj,name="deletecartobj"),
    path("checkout/",views.checkout,name="checkout"),
    path("viewcart/",views.viewcart,name="viewcart"),
    path("addpro/",views.addpro,name="addproduct"),
    # path("payment/",views.payment,name="payment"),
    # path("payment/succ",views.payment_success,name="paysuccess"),
    path("payment/success",views.payment_failure,name="payfailure"),
    path("makepayment/",views.makepayment,name="makepayment"),
    path("viewpdf/",views.pdf_view,name="viewpdf"),
    path("addproduct/",views.insertproduct,name="addproduct"),
    path("showprodlist/",views.showprodlist,name="editprolist"),
    path('pay/', views.initiate_payment, name='pay'),
    
]