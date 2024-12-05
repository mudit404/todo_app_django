from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import ToDoItem, Tag
from .serializers import ToDoItemSerializer, TagSerializer

class ToDoItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet to handle all CRUD operations for ToDoItem
    """
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Override create to handle tags separately.
        """
        data = request.data
        tags_data = data.pop('tags', [])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()

        # Handle tags
        for tag_name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            todo.tags.add(tag)

        headers = self.get_success_headers(serializer.data)
        return Response(self.get_serializer(todo).data, status=status.HTTP_201_CREATED, headers=headers)

class TagViewSet(viewsets.ModelViewSet):
    """
    ViewSet to handle CRUD operations for Tags.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
