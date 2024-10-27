from rest_framework import serializers
from escola.models import Estudante,Curso,Matricula
from escola.validators import validate_celular, validate_nome, validate_cpf

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'
    
    def validate(self, data) : 
        
        if validate_cpf(data['cpf']) :
            raise serializers.ValidationError({'O CPF deve ser válido'})
        
        if validate_nome(data['nome']) :
             raise serializers.ValidationError({'O NOME só pode conter letras'})

        if validate_celular(data['celular']) :
             raise serializers.ValidationError({'O celular precisa seguir o modelo: 99 99999-9999'})
        
        return data
    
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']