from rest_framework import serializers
from ads.models import Ad, Comment
from users.models import User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field= "first_name"
    )

    class Meta:
        model = Comment
        exclude = ['ad']


class CommentCreateSerializer(serializers.ModelSerializer):
    ad = serializers.SlugRelatedField(
        queryset = Ad.objects.all(),
        slug_field="id",
        required = True
    )

    author = serializers.SlugRelatedField(
        queryset = User.objects.all(),
        slug_field= "id",
        required = True
    )

    class Meta:
        model = Comment
        fields = '__all__'
    

class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field= "first_name"
    )

    class Meta:
        model = Ad
        exclude = ['description']


class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field= "first_name"
    )

    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset = User.objects.all(),
        slug_field= "first_name"
    )

    class Meta:
        model = Ad
        fields = '__all__'
