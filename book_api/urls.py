from django.conf.urls import url
from django.urls import path
from graphene_django.views import GraphQLView
import graphql

urlpatterns = [
    path('graphene/', GraphQLView.as_view(graphiql=True)),
]