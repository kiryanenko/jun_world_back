from rest_framework import serializers

from level.models import UserLevelProgress, Level


class AddLevelProgressSerializer(serializers.ModelSerializer):
    level = serializers.SlugRelatedField(slug_field='num', queryset=Level.objects.all())

    class Meta:
        model = UserLevelProgress
        fields = ('level', 'points')

    def create(self, validated_data):
        level = validated_data.get('level')
        points = validated_data.get('points')

        progress = UserLevelProgress.objects.update_or_create(user=self.context['request'].user, level=level,
                                                              defaults={'points': points})
        self.context['request'].user.rating += points
        self.context['request'].user.save()
        return progress
