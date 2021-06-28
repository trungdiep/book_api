from django.db import models
import graphene

from graphene_django import DjangoObjectType, DjangoListField
from .models import Book

class BookType(DjangoObjectType): 
    class Meta:
        model = Book
        fields = "__all__"

    
class Query(graphene.ObjectType):
    all_block = graphene.List(BookType)
    book_id = graphene.Field(BookType, book_id=graphene.Int())

    def resolve_all_books(self, root, **kwargs):
        return Book.objects.all()

    def resolve_book(self, root, id):
        return Book.objects.filter(pk=id)

class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    year_published = graphene.String()
    review = graphene.Int()

class CreateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, data_book=None):
        book_instance = Book(
            title=data_book.title,
            author=data_book.author,
            year_published=data_book.year_published,
            review=data_book.review   
        )
        book_instance.save()
        return CreateBook(book=book_instance)

class UpdateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, data_book):
        book_instance = Book.objects.get(pk=data_book.id)
        if book_instance:
            book_instance.title =  data_book.title
            book_instance.author = data_book.author
            book_instance.year_published = data_book.year_published
            book_instance.review = data_book.review
        
            return UpdateBook(book=book_instance)
        return UpdateBook(block=None)

class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(BookType)

    def mutate(root, info, id):
        book = Book.objects.get(id=id)
        book.delete()
        return None

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook()


schema = graphene.Schema(query=Query, mutation=Mutation)

