from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views



router=routers.DefaultRouter()
router.register('',views.CourseView)
router.register('user',views.UserView)


urlpatterns = [
    path('v1/',include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]