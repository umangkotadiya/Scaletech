from rest_framework import generics, permissions, status ,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from .models import User, Role
from .serializers import UserSerializer, RoleSerializer
       

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def add_access_module(self, request, pk=None):
        role = self.get_object()
        new_module = request.data.get('module')
        if new_module not in role.access_modules:
            role.access_modules.append(new_module)
            role.save()
            return Response(role.access_modules, status=status.HTTP_200_OK)
        return Response({"detail": "Module already exists."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def remove_access_module(self, request, pk=None):
        role = self.get_object()
        module_to_remove = request.data.get('module')
        if module_to_remove in role.access_modules:
            role.access_modules.remove(module_to_remove)
            role.save()
            return Response(role.access_modules, status=status.HTTP_200_OK)
        return Response({"detail": "Module does not exist."}, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'login']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
 
    @action(detail=False, methods=['put'], permission_classes=[permissions.IsAuthenticated])
    def bulk_update(self, request):
        ids = request.data.get('ids', [])
        last_name = request.data.get('last_name')
        if last_name is not None:
            User.objects.filter(id__in=ids).update(last_name=last_name)
            return Response({"detail": "Users updated successfully."}, status=status.HTTP_200_OK)
        return Response({"detail": "Last name is required."}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        search = request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(username__icontains=search)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

