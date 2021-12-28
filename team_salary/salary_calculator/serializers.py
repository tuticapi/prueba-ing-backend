from rest_framework import serializers

class MemberSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True)
    nivel = serializers.CharField(required=True)
    goles = serializers.IntegerField(required=True)
    sueldo = serializers.DecimalField(
        decimal_places=2,
        required=True
    )
    bono = serializers.DecimalField(
        decimal_places=2,
        required=True
    )
    sueldo_completo = serializers.DecimalField(
        decimal_places=2,
        required=True
    )
    equipo = serializers.CharField(required=True)