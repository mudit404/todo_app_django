from rest_framework import serializers
from .models import ToDoItem, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ToDoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = ToDoItem
        fields = "__all__"
