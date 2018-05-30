from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from passenger_census_api import views
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'PassengerCensus', views.PassengerCensusViewSet)
router.register(r'PassengerCensus', views.PassengerCensusRetrieveViewSet)
router.register(r'PassengerCensusRoutesAnnual', views.PassengerCensusRoutesAnnualViewSet, base_name='PassengerCensus')

# schema_view = get_swagger_view(title='Hack Oregon 2018 Transportation Systems APIs')

urlpatterns = [
    # url(r'^schema/', schema_view),
    url(r'^', include(router.urls)),
    # url(r'^api/', include(router.urls)),
]
