from enum import Enum

class EnumMenuMessage(Enum):
    PRESENTATION_MESSAGE = {
        'pt_BR': "Obrigado por usar esse programa!\nPor favor escolha alguma operação use 0(zero) para sair!",
    }
    MENU_OPTIONS_MESSAGE = {
        'pt_BR': ['Adicionar programação', 'Consultar programação', 'Sair']
    }
    INPUT_CHOOSE_OPTION_MESSAGE = {
        'pt_BR': "Escolha uma opção: "
    }
    EXIT_MESSAGE = {
        'pt_BR': "Saindo do menu. Obrigado!"
    }
    WRONG_OPTION_MESSAGE = {
        'pt_BR': "Opção inválida. Tente novamente."
    }
    CREATE_SUCCESS_MESSAGE = {
        "pt_BR": "Programa adicionado com sucesso!",
    }
    CREATE_MESSAGE = {
        "pt_BR": "Por favor digite a programação a ser adicionada!\n",
    }
    QUERY_MESSAGE = {
        "pt_BR": "Por favor digite a programação a ser adicionada!\n",
    }
    PROCESS_INPUT_ERROR_MESSAGE = {
        "pt_BR": "Houve uma falha na sintaxe digitada.",
    }
    CREATE_FAILURE_MESSAGE = {
        "pt_BR": "Falha ao adicionar um programa. Verifique os dados fornecidos.",
    }
    QUERY_SUCCESS_MESSAGE = {
        "pt_BR": "Detalhes do programa: {}",
    }
    QUERY_FAILURE_MESSAGE = {
        "pt_BR": "Programa não encontrado.",
    }
