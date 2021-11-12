from rest_framework import viewsets, status
from rest_framework.response import Response

from snippet_app.models import Snippet, Tag
from snippet_app.serializers import SnippetSerializer, TagSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        snippet = Snippet.objects.filter(tag=instance)
        data['snippets'] = SnippetSerializer(snippet, many=True, context={'request': request}).data
        return Response(data, status=status.HTTP_200_OK)
