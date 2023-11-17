from rest_framework import serializers
from .models import Singer, Song 



class SingerSerializer (serializers.ModelSerializer):
    # here song is related name of foregine key in model is way to get data of other model
    # this text field many not to get id get text field. # we have also so many key . 
    song  = serializers.StringRelatedField(many=True , read_only=True)
    # song  = serializers.PrimaryRelatedField(many=True , read_only=True) give pk 
    # song  = serializers.HyperLinkedRelatedField(read_only=True , view_name="give whatever you want to give name")
    # song  = serializers.RelatedField(read_only=True , many=true , slug-field="title / duration /  .")
    class Meta: 
        model = Singer 
        fields = [ 'id' , 'name' , 'gender' , 'song' ]



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song 
        fields = [ 'id' , 'title' , 'singer' ,  'duration']
    



#  hyper linked modelserializer it give you api as url like  : -----------------


# Give you a list of your old aldi product or images or maybe whatever you want to store it give you a link and that link whenever you click it the link give you the particular data detail view

class Singer_Song(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Singer 
        fields = ['id'  , 'url' ,'name' , 'gender' ,]

# repr is used to ckeck what happen inside a function code .