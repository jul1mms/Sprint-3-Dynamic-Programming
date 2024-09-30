import json

dados_json = [
    {
        "procedimento": "laparoscopia",
        "nivel": 3,
        "data": "09/01/2024",
        "tempo": "2h",
        "instrumentos": ["bisturi", "pinça", "cauterizador"],
        "pontuacao": {
            "precisao": 8,
            "tempo": 7,
            "uso_instrumentos": 9,
            "geral": 8
        },
        "falhas": ["Demora para cauterizar."],
        "notas": "Precisão pode melhorar."
    },
    {
        "procedimento": "colecistectomia laparoscópica",
        "nivel": 2,
        "data": "10/01/2024",
        "tempo": "1h 30m",
        "instrumentos": ["bisturi", "pinça", "grampeador cirúrgico"],
        "pontuacao": {
            "precisao": 6,
            "tempo": 5,
            "uso_instrumentos": 6,
            "geral": 5.7
        },
        "falhas": ["Sangramento excessivo devido a má manipulação."],
        "notas": "Deve revisar técnicas de sutura."
    },
    {
        "procedimento": "cirurgia endoscópica do joelho",
        "nivel": 4,
        "data": "12/01/2024",
        "tempo": "3h",
        "instrumentos": ["endoscópio", "shaver", "grampeador cirúrgico"],
        "pontuacao": {
            "precisao": 9,
            "tempo": 8,
            "uso_instrumentos": 9,
            "geral": 8.7
        },
        "falhas": [],
        "notas": "Ótima precisão e controle de tempo."
    },
    {
        "procedimento": "laparoscopia",
        "nivel": 3,
        "data": "14/01/2024",
        "tempo": "2h 10m",
        "instrumentos": ["bisturi", "pinça", "cauterizador"],
        "pontuacao": {
            "precisao": 7,
            "tempo": 6,
            "uso_instrumentos": 7,
            "geral": 6.7
        },
        "falhas": ["Atraso no controle de sangramento."],
        "notas": "Controle de hemorragia deve ser aprimorado."
    },
    {
        "procedimento": "cirurgia endoscópica do ombro",
        "nivel": 1,
        "data": "15/01/2024",
        "tempo": "1h 50m",
        "instrumentos": ["endoscópio", "shaver", "pinça"],
        "pontuacao": {
            "precisao": 5,
            "tempo": 4,
            "uso_instrumentos": 5,
            "geral": 4.7
        },
        "falhas": ["Posicionamento incorreto do endoscópio."],
        "notas": "Precisa melhorar a coordenação entre instrumentos."
    },
    {
        "procedimento": "colecistectomia laparoscópica",
        "nivel": 2,
        "data": "18/01/2024",
        "tempo": "1h 40m",
        "instrumentos": ["bisturi", "pinça", "grampeador cirúrgico"],
        "pontuacao": {
            "precisao": 7,
            "tempo": 7,
            "uso_instrumentos": 8,
            "geral": 7.3
        },
        "falhas": [],
        "notas": "Melhor desempenho, boa recuperação."
    },
    {
        "procedimento": "laparoscopia",
        "nivel": 4,
        "data": "20/01/2024",
        "tempo": "2h 15m",
        "instrumentos": ["bisturi", "pinça", "cauterizador"],
        "pontuacao": {
            "precisao": 9,
            "tempo": 8,
            "uso_instrumentos": 9,
            "geral": 8.7
        },
        "falhas": [],
        "notas": "Excelente controle e precisão."
    },
    {
        "procedimento": "cirurgia laparoscópica de hérnia inguinal",
        "nivel": 3,
        "data": "22/01/2024",
        "tempo": "2h 5m",
        "instrumentos": ["bisturi", "pinça", "cauterizador"],
        "pontuacao": {
            "precisao": 8,
            "tempo": 6,
            "uso_instrumentos": 7,
            "geral": 7
        },
        "falhas": ["Movimentos imprecisos ao manipular a pinça."],
        "notas": "Melhorar controle em espaços reduzidos."
    },
    {
        "procedimento": "laparoscopia",
        "nivel": 2,
        "data": "23/01/2024",
        "tempo": "1h 45m",
        "instrumentos": ["bisturi", "pinça", "cauterizador"],
        "pontuacao": {
            "precisao": 5,
            "tempo": 6,
            "uso_instrumentos": 4,
            "geral": 5
        },
        "falhas": ["Ação tardia ao usar o cauterizador.", "Erros repetidos ao segurar o bisturi."],
        "notas": "Faltou agilidade e precisão."
    },
    {
        "procedimento": "cirurgia laparoscópica de apendicite",
        "nivel": 4,
        "data": "24/01/2024",
        "tempo": "2h 30m",
        "instrumentos": ["bisturi", "cauterizador", "trocater"],
        "pontuacao": {
            "precisao": 9,
            "tempo": 8,
            "uso_instrumentos": 9,
            "geral": 8.7
        },
        "falhas": [],
        "notas": "Excelente precisão e uso de instrumentos."
    },
    {
        "procedimento": "cirurgia endoscópica da coluna vertebral",
        "nivel": 1,
        "data": "25/01/2024",
        "tempo": "3h",
        "instrumentos": ["endoscópio", "bisturi", "pinça"],
        "pontuacao": {
            "precisao": 4,
            "tempo": 3,
            "uso_instrumentos": 5,
            "geral": 4
        },
        "falhas": ["Desorientação com o endoscópio.", "Muitos erros ao manipular a pinça."],
        "notas": "Precisa revisar fundamentos de uso de endoscópio."
    },
    {
        "procedimento": "cirurgia laparoscópica de vesícula biliar",
        "nivel": 2,
        "data": "26/01/2024",
        "tempo": "1h 55m",
        "instrumentos": ["bisturi", "pinça", "cauterizador"],
        "pontuacao": {
            "precisao": 6,
            "tempo": 5,
            "uso_instrumentos": 6,
            "geral": 5.7
        },
        "falhas": ["Atraso em realizar a incisão inicial."],
        "notas": "Agilidade precisa melhorar."
    },
    {
        "procedimento": "cirurgia endoscópica do quadril",
        "nivel": 4,
        "data": "27/01/2024",
        "tempo": "2h 20m",
        "instrumentos": ["endoscópio", "shaver", "pinça"],
        "pontuacao": {
            "precisao": 9,
            "tempo": 9,
            "uso_instrumentos": 9,
            "geral": 9
        },
        "falhas": [],
        "notas": "Desempenho excepcional."
    },
    {
        "procedimento": "colecistectomia laparoscópica",
        "nivel": 1,
        "data": "28/01/2024",
        "tempo": "1h 40m",
        "instrumentos": ["bisturi", "pinça", "grampeador cirúrgico"],
        "pontuacao": {
            "precisao": 5,
            "tempo": 4,
            "uso_instrumentos": 5,
            "geral": 4.7
        },
        "falhas": ["Erros de posicionamento do grampeador."],
        "notas": "Necessita mais prática com instrumentos."
    }
]

def carregar_dados_json():
    with open('dados.json', 'r') as f:
        return json.load(f)