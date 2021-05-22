from rest_framework import serializers
from .models import Review, Comment

class CommentSerializer(serializers.ModelSerializer):

    def getUsername(self, obj):
        return obj.user.username

    username = serializers.SerializerMethodField("getUsername")

    class Meta:
        model = Comment
        fields = ('id','content','username','created_at',)
        read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True) # read_only는 유효성검사에는 들어가지 않고 오직 읽을 때만 사용
    comment_count = serializers.IntegerField(
        source='comment_set.count', 
        read_only=True
    )
    def getUsername(self, obj):
        return obj.user.username
        
    username = serializers.SerializerMethodField("getUsername")

    class Meta:
        model = Review
        fields = ('id','title','username','content','comment_count','comment_set','created_at',)
        depth = 1
        

