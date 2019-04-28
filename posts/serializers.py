from rest_framework import serializers
from posts.models import Post, User


class PostSerializer(serializers.HyperlinkedModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')

	class Meta:
		model = Post
		fields = ('url', 'author', 'title', 'body')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

	class Meta:
		model = User
		fields = ('url', 'email', 'username', 'first_name', 'last_name', 'password', 'posts')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		password = validated_data.pop('password')
		user = User(**validated_data)
		user.set_password(password)
		user.save()
		return user

	def update(self, instance, validated_data):
		password = validated_data.pop('password')
		instance.set_password(password)
		instance.email = validated_data.get('email', instance.email)
		instance.username = validated_data.get('username', instance.username)
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.save()
		return instance
