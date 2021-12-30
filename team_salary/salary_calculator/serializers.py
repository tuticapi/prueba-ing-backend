from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True)
    goles = serializers.IntegerField(required=True)
    sueldo = serializers.DecimalField(
        max_digits=20,
        decimal_places=2,
        required=True
    )
    bono = serializers.DecimalField(
        max_digits=20,
        decimal_places=2,
        required=True
    )    
    sueldo_completo = serializers.DecimalField(
        max_digits=20,
        decimal_places=2,
        allow_null=True
    )
    equipo = serializers.CharField(required=True)


class MemberSerializer(BaseSerializer):
    nivel = serializers.CharField(required=True)


class MemberSalarySerializer(BaseSerializer):
    goles_minimos = serializers.IntegerField(required=True)
