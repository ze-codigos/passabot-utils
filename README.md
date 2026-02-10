# PassaBot Utils

Biblioteca de funções auxiliares para agentes PassaBot.

## Instalação

### Instalação via pip (local)

```bash
pip install -e /home/ferna/Passabot/passabot-utils
```

### Instalação via GitHub (quando publicar)

```bash
pip install git+https://github.com/passabot/passabot-utils.git
```

### Instalação via PyPI (quando publicar)

```bash
pip install passabot-utils
```

## Uso

### trim_messages_from_state

Remove mensagens antigas e problemáticas mantendo apenas as mais recentes.

```python
from passabot_utils import trim_messages_from_state

# Lista de mensagens
messages = [
    {"role": "user", "content": "Olá"},
    {"role": "assistant", "content": "Oi!"},
    # ... mais mensagens
]

# Manter apenas as 20 últimas mensagens válidas
messages_trimmed = trim_messages_from_state(messages, qtd_mensagens=20)
```

### Parâmetros

- `messages` (List): Lista de mensagens da conversa
- `qtd_mensagens` (int, opcional): Quantidade de mensagens a manter. Padrão: 20

### Retorno

Lista de mensagens filtrada, removendo:
- Mensagens antigas (mantém apenas as N mais recentes)
- Mensagens de ferramenta (`role: "tool"`) no início
- Mensagens vazias no início
- Mensagens de assistente com `tool_calls` no início

## Desenvolvimento

### Estrutura do projeto

```
passabot-utils/
├── passabot_utils/
│   ├── __init__.py
│   └── message_trimmer.py
├── setup.py
├── pyproject.toml
└── README.md
```

### Build e publicação

```bash
# Instalar ferramentas de build
pip install build twine

# Criar distribuição
python -m build

# Publicar no PyPI (quando estiver pronto)
twine upload dist/*
```

## Licença

MIT License

