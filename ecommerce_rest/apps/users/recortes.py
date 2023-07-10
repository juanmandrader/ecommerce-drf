class TestUserSerializer(serializers.Serializer):
    # Serializador de prueba
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()

    def validate_name(self,value):
        # validacion personalizada
        if "developer" in value:
            raise serializers.ValidationError("Error, no puede existir un usuario que contenga developer")
        return value

    def validate_email(self,value):
        # validacion correo no vacio
        if value == "":
            raise serializers.ValidationError("Tiene que indicar un correo")
        # validacion correo no contenga el nombre
        """if self.validate_name(self.context["name"]) in value:
            raise serializers.ValidationError("El email no puede contener el nombre")"""            
        return value

    def validate(self,data):
        return data

    def create(self,validated_data):
        return User.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance

    def save(self):
        print(self.validated_data)
        # otras funciones como enviar emails, etc, pero que no 
        # se guarde la información en la BD

##################################################################################

##################################################################################
"""
class UserAPIView(APIView):
    
    def get(self,request):
        users = User.objects.all()
        users_serializer = UserSerializer(users,many=True)
        return Response(users_serializer.data)
"""

