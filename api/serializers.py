from Task.models import User
from rest_framework import serializers
from Task.models import Task,Catagory

class UserSerializer(serializers.ModelSerializer):
   class Meta:
        model = User
        fields = ['username', 'email']
class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory 
        fields= ['id','name']       
class TaskSerializer(serializers.ModelSerializer):
    catagory = CatagorySerializer(read_only=True)
    catagory_id = serializers.PrimaryKeyRelatedField(queryset=Catagory.objects.all(), source='catagory', write_only=True)
    class Meta:
        model = Task
        fields = "__all__"
    def validate_status(self, value):
        task = self.instance
        if task and task.status == Task.COMPLETED and value != Task.COMPLETED:
            raise serializers.ValidationError("Completed tasks cannot be changed to another status unless reverted to incomplete.")
        return value

   