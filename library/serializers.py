from unicodedata import category

from rest_framework import serializers

from .models import Author, Book, Category, Publisher


class BookSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Category.objects.all())
    category_name = serializers.CharField(
        source='category.name', read_only=True)
    author = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Author.objects.all())
    author_name = serializers.CharField(source='author.name', read_only=True)
    publisher = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Publisher.objects.all())
    publisher_name = serializers.CharField(
        source='publisher.name', read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'category', 'category_name', 'author', 'author_name', 'publisher', 'publisher_name', 'published_date',
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
