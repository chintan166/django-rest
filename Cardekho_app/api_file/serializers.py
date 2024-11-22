from rest_framework import serializers
from ..models import Carlist,Showroomlist,Review

def alphanumberic(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("only alphanumeric characeter are allowed")
    
class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        
class CarSerializer(serializers.ModelSerializer):
    Reviews = ReviewSerializers(many=True,read_only=True)
    class Meta:
        model = Carlist
        fields = "__all__"
        
    def validate_price(self,value):
        if value <= 20000:
            raise serializers.ValidationError("price must be greater than 20000")
        return value
    
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description must be different")
        return data
    
class ShowroomSerializer(serializers.ModelSerializer):
    Showrooms = CarSerializer(many=True,read_only=True)
    class Meta:
        model = Showroomlist
        fields = "__all__"
        
