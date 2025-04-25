from rest_framework import serializers

from join_app.models import Task, Category, Contact, Subtask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['end_date', 'priority', 'state']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        address_fields = ['street', 'zip_code', 'city']
        address = {field: data.pop(field) for field in address_fields if field in data}

        data['address'] = address
        return data

class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'surname', 'email', 'badge_color']