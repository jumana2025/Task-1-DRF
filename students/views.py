from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer, StudentDetailSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentSerializer