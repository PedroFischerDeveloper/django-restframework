
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.UserView import UserView
from api.views.BankAccountView import BankAccountView
from api.views.TransactionView import TransactionView
from api.views.home import HomeView



urlpatterns = [
    path('', HomeView),
    path('admin/', admin.site.urls),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/users/', UserView.as_view(), name='users'),
    path('api/users/<int:id>/', UserView.as_view(), name='get_user'),
    path('api/users/create', UserView.as_view(), name='create_user'),

    path('api/account/', BankAccountView.as_view(), name='accounts'),
    path('api/account/<int:id>/', BankAccountView.as_view(), name='get_account'),
    path('api/account/create', BankAccountView.as_view(), name='create_account'),  

    path('api/transactions/', TransactionView.as_view(), name='transactions'),
    path('api/transactions/<int:id>/', TransactionView.as_view(), name='get_transaction'),
    path('api/transactions/create', TransactionView.as_view(), name='create-transaction'),  

]
