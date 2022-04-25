from .models import Location, Park, Breed, Gender, Socialization, Aggression, Tag, Size, User, Dog, Image, Connection, Conversation, Message, Comment
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LocationSerializer, ParkSerializer, BreedSerializer, GenderSerializer, SocializationSerializer, AggressionSerializer, TagSerializer, SizeSerializer, UserSerializer, DogSerializer, ImageSerializer, ConnectionSerializer, ConversationSerializer, MessageSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Locations to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ParkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Park.objects.all()
    serializer_class = ParkSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows a Park view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class BreedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows an Breed view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class GenderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows a Gender view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class SocializationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Socialization.objects.all()
    serializer_class = SocializationSerializer
    """
    ^ Allows a Socialization view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class AggressionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Aggression.objects.all()
    serializer_class = AggressionSerializer
    """
    ^ Allows a Aggression view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows a todo view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class SizeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sizes to be viewed or edited.
    """
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows a User view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class DogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows an Dog view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows a Image view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class ConnectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    """
    ^ Allows a Connection view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    """
    ^ Allows a Conversation view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows a Message view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows a Comment view searching by user name bc of the foreign key relation with user_id or simply by user id
    """