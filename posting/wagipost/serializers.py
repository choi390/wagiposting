from rest_framework import serializers
from .models import Post, PostImage

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']


class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    image_files = serializers.ListField(
        child=serializers.ImageField(),  # 이미지 여러 개 받을 수 있도록
        write_only=True,
        required=False
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'images', 'image_files']
        
    def create(self, validated_data):
        image_files = validated_data.pop('image_files', [])  # image_files 제거하고 따로 저장
        post = Post.objects.create(**validated_data)         # 실제 Post 모델 필드만 사용
        for image in image_files:
            PostImage.objects.create(post=post, image=image)
        return post