from rest_framework import serializers

from snippet_app.models import Snippet, Tag


class SnippetSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="snippets-detail")

    class Meta:
        model = Snippet
        fields = ('id', 'url', 'created_on', 'title', 'content')
        read_only_fields = ['created_user']

    def create(self, validated_data):
        user = self.context['request'].user
        if not user.is_authenticated:
            raise serializers.ValidationError(detail='User not logged in')
        validated_data['created_user'] = user
        return super(SnippetSerializer, self).create(validated_data)


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"

