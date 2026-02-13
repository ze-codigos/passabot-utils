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


## 📜 License

This project is licensed under the Apache License 2.0.

You are free to use, modify, and distribute this software, including for commercial purposes, provided that you include the original copyright and license notice.

See the [LICENSE](LICENSE) file for more details.



