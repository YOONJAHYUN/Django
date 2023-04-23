from django.shortcuts import render
from .models import Actor, Movie, Review
from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer, ActordetailSerializer, TitleSerializer, MoviedetailSerializer, ReviewsSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = get_list_or_404(Actor)
        serializers = ActorSerializer(actors, many=True)
        return Response(serializers.data)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    if request.method == 'GET':
        actor = get_object_or_404(Actor, pk=actor_pk)
        serializer = ActordetailSerializer(actor)
        return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializers = MovieSerializer(movies, many=True)
        return Response(serializers.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MoviedetailSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializers = ReviewsSerializer(reviews, many=True)
        return Response(serializers.data)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review)
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        result = {}
        result['delete'] = f'review {review_pk} is deleted'
        return Response(result)


@api_view(['POST'])
def create_review(request, movie_pk):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)