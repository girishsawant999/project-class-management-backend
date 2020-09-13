from rest_framework import viewsets, permissions

from .models import Student
from .serializers import StudentSerializer


# Create your views here.


class StudentViewset(viewsets.ModelViewSet):
    # def get_queryset(self):
    #     user = self.request.query_params.get('user')
    #     queryset = Customer.objects.filter(user=user)
    #     return queryset

    queryset = Student.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer
