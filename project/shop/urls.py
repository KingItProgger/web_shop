from django.urls import path
from .views import ProductsSofaList,ProductDetail,ProductCreate,ProductUpdate,ProductDelete,ProductsFurnitureList,ProductsTablesList,ProductsFireplaceList, SofaCornerList,SofaStraightList,SofaTransList,Search

urlpatterns = [
    path('',ProductsSofaList.as_view(),name='products_sofa_list'),
    path('furniture/',ProductsFurnitureList.as_view(),name='products_furniture_list'),
    path('fireplaces/',ProductsFireplaceList.as_view(),name='products_fireplaces_list'),
    path('tables/',ProductsTablesList.as_view(),name='products_tables_list'),
    path('<int:pk>/',ProductDetail.as_view(),name='product_detail'),
    path('create/',ProductCreate.as_view(),name='product_create'),
    path('<int:pk>/update/',ProductUpdate.as_view(),name='product_edit'),
    path('<int:pk>/delete/',ProductDelete.as_view(),name='product_delete'),
    path('corner/',SofaCornerList.as_view(),name='sofa_corner'),
    path('straight/', SofaStraightList.as_view(), name='sofa_straight'),
    path('transformer/', SofaTransList.as_view(), name='sofa_trans'),
    path('search/',Search.as_view(),name='search')

]