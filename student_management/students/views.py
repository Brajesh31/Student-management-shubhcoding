# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     @action(detail=False, methods=['get'])
#     def search(self, request):
#         roll = request.query_params.get('roll_number')
#         if roll:
#             student = Student.objects.filter(roll_number=roll).first()
#             if student:
#                 return Response(self.get_serializer(student).data)
#         return Response({"error": "Not found"}, status=404)

#     @action(detail=True, methods=['post'])
#     def mark_attendance(self, request, pk=None):
#         student = self.get_object()
#         student.attendance += 1
#         student.save()
#         return Response({"attendance": student.attendance})

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404
from bson import ObjectId  # import from pymongo or bson package

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_object(self):
        pk = self.kwargs.get("pk")
        try:
            obj = get_object_or_404(Student, pk=ObjectId(pk))
        except Exception:
            raise Response({"detail": "Invalid ID format"}, status=400)
        return obj

    @action(detail=False, methods=['get'])
    def search(self, request):
        roll = request.query_params.get('roll_number')
        if roll:
            student = Student.objects.filter(roll_number=roll).first()
            if student:
                return Response(self.get_serializer(student).data)
        return Response({"error": "Not found"}, status=404)

    @action(detail=True, methods=['post'])
    def mark_attendance(self, request, pk=None):
        student = self.get_object()
        student.attendance += 1
        student.save()
        return Response({
            "message": f"Attendance marked for {student.name}",
            "attendance": student.attendance
        })
