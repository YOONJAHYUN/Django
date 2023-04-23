from .models import Movie, Review, Actor
from rest_framework import serializers

class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', )

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview')


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content')

class ReviewSerializer(serializers.ModelSerializer):
    movie = TitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

class ActordetailSerializer(serializers.ModelSerializer):
    movies = TitleSerializer(read_only=True, many=True)

    class Meta:
        model = Actor
        fields = '__all__'

class MoviedetailSerializer(serializers.ModelSerializer):

    class ActorsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name', )

    actors = ActorsSerializer(many=True)
    review_set = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'






