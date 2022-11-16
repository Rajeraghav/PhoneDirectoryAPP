from django.urls import path
from . import views
from . import apiviews
app_name = "LibraryManagementSystem"
urlpatterns = [
    #path('', views.index, name= 'index'),
    path('', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('delete/<int:id>', views.bookdelete, name="bookdelete"),
    path('update/<int:id>', views.bookupdate, name='bookupdate'),
    path('dobookupdate/<int:id>', views.dobookupdate, name='dobookupdate'),
    path('search/', views.SearchView.as_view(), name='search'),
    #path('add-to-cart/', views.AddToCart(), name='addToCart')
    path('getBook/<int:id>', views.getBook, name="getBook"),
    path('returnBook/<int:id>', views.returnBook, name="returnBook"),
    path('logout/', views.logout_view, name='logout'),
    path('addUser', views.addUser, name='addUser')
]
urlpatterns += [
    path('api/', apiviews.apiOverview),
    path('api/admin/bookList/', apiviews.bookList),
    path('api/admin/bookDetail/<str:pk>/', apiviews.bookDetail),
    path('api/admin/addbook/', apiviews.bookCreate),
    path('api/admin/updateBook/<str:pk>/', apiviews.bookUpdate),
    path('api/admin/deleteBook/<str:pk>/', apiviews.bookDelete),
    path('api/admin/user-list/', apiviews.userList),
    path('api/admin/addUser/', apiviews.user),
]
urlpatterns += [
    path('api/search/<str:pk>/', apiviews.booksearch),
    path('api/payment-list/', apiviews.paymentList),
    path('api/payment/', apiviews.payment),
    path('api/lend/', apiviews.lendBook),
    path('api/return/<str:pk>/', apiviews.returnBook),
]
