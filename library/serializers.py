from rest_framework import serializers

from .models import Author, Book, Category, Publisher


class CategorySerializer(serializers.ModelSerializer):
    # quizzes = QuizSerializer(many=True, write_only=True)
    # quiz_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', )

    # def get_quiz_count(self, obj):
    #     return obj.quizzes.count()
