from rest_framework import viewsets, filters
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser] 
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    

    # 이미지 업로드 위해 필요
    '''
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()

        # 이미지 여러 개 처리
        image_files = request.FILES.getlist('image_files')
        for image in image_files:
            PostImage.objects.create(post=post, image=image)

            return Response(self.get_serializer(post).data, status=status.HTTP_201_CREATED)
            '''