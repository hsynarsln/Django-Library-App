from unicodedata import category

from rest_framework import serializers

from .models import Author, Book, Category, Publisher


class BookSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    # author = serializers.StringRelatedField()
    # publisher = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ('id', 'title', 'category', 'author', 'publisher', 'published_date',
                  'total_pages', 'description', 'created_date', 'updated_date')


class CategorySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    book_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'book_count', 'books')

    def get_book_count(self, obj):
        return obj.books.count()


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    book_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'book_count', 'books')

    def get_book_count(self, obj):
        return obj.books.count()


class PublisherSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    book_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'book_count', 'books')

    def get_book_count(self, obj):
        return obj.books.count()
