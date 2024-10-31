class ErrorMessages:
    messages = {
        'USER_EXISTS': 'Usuário já cadastrado',
        'NOT_FOUND': 'Usuário não localizado',
        'INVALID_DATE': 'Dado Inválido',
    }

    @classmethod
    def get_error(cls, key):
        return {'error': cls.messages.get(key, 'Erro desconhecido')}