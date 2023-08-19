from .serializers import UserSerializer,CoursesSerializer,StudentSerializer,TeacherSerializer, LoginSerializer
from home.models import User,Courses,Student,Teacher
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView


class UserModelView(APIView):
    
    def post(self, request):
        try:
            data=request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        try:
            data=User.objects.all()
            serializer=UserSerializer(data, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class UserModelView1(APIView):
    
    def put(self, request, pk):
        try:
            data=User.objects.get(id=pk)
            serializer = UserSerializer(instance=data, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            data=User.objects.get(id=pk)
            data.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, pk):
        try:
            data=User.objects.get(id=pk)
            serializer=UserSerializer(data)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
class CourseModelView(APIView):
    
    def post(self, request):
        try:
            data=request.data
            serializer = CoursesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        try:
            data=Courses.objects.all()
            serializer=CoursesSerializer(data, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class CourseModelView1(APIView):
    
    def put(self, request, pk):
        try:
            data=Courses.objects.get(id=pk)
            serializer = CoursesSerializer(instance=data, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            data=Courses.objects.get(id=pk)
            data.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, pk):
        try:
            data=Courses.objects.get(id=pk)
            serializer=CoursesSerializer(data)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
        
class StudentModelView(APIView):
    
    def post(self, request):
        try:
            data=request.data
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        try:
            data=Student.objects.all()
            serializer=StudentSerializer(data, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class StudentModelView1(APIView):
    
    def put(self, request, pk):
        try:
            data=Student.objects.get(id=pk)
            serializer = StudentSerializer(instance=data, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            data=Student.objects.get(id=pk)
            data.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, pk):
        try:
            data=Student.objects.get(id=pk)
            serializer=StudentSerializer(data)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
        
class TeacherModelView(APIView):
    
    def post(self, request):
        try:
            data=request.data
            serializer = TeacherSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        try:
            data=Teacher.objects.all()
            serializer=TeacherSerializer(data, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class TeacherModelView1(APIView):
    
    def put(self, request, pk):
        try:
            data=Teacher.objects.get(id=pk)
            serializer = TeacherSerializer(instance=data, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            data=Teacher.objects.get(id=pk)
            data.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, pk):
        try:
            data=Teacher.objects.get(id=pk)
            serializer=TeacherSerializer(data)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
        
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)