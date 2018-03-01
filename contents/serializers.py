from rest_framework import serializers
from contents.models import userAdmin,userProfile

class userAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = userAdmin
        fields =('username','password')

class userProfileSerializer(serializers.ModelSerializer):
    eye = serializers.ImageField(max_length=None,use_url=True)
    face = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = userProfile
        fields = '__all__'
