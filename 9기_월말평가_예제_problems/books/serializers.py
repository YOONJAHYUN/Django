from rest_framework import serializers
from .models import Book

# Q 1.
class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'content')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
