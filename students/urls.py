from rest_framework import routers

from .views import StudentViewset

router = routers.DefaultRouter()
router.register('api/students', StudentViewset, 'students')

urlpatterns = router.urls
