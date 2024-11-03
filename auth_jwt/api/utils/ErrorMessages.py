class ErrorMessages:
    messages = {
        'USER_EXISTS': 'Usuário já cadastrado',
        'NOT_FOUND': 'Recurso não localizado',
        'INVALID_DATE': 'Dado Inválido',
        'PAGED_NOT_RESULT': 'A Consulta não trouxe resultados!'
    }

    @classmethod
    def get_error(cls, key):
        return {'error': cls.messages.get(key, 'Erro desconhecido')}