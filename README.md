# PassaBot Utils

Biblioteca de funções auxiliares para agentes PassaBot.

## Instalação

### Instalação via pip (local)

Clone o repositório e instale em modo desenvolvimento:

```bash
git clone https://github.com/passabot/passabot-utils.git
cd passabot-utils
pip install -e .
```

### Instalação via GitHub

```bash
pip install git+https://github.com/ze-codigos/passabot-utils.git
```

### Instalação via PyPI (quando publicar)

```bash
pip install passabot-utils
```

## Uso

### trim_messages

Remove mensagens antigas e problemáticas mantendo apenas as mais recentes.

```python
from passabot_utils import trim_messages

# Lista de mensagens
messages = [
    {"role": "user", "content": "Olá"},
    {"role": "assistant", "content": "Oi!"},
    # ... mais mensagens
]

# Manter apenas as 20 últimas mensagens válidas
messages_trimmed = trim_messages(messages, qtd_mensagens=20)
```

**Parâmetros:**
- `messages` (List): Lista de mensagens da conversa
- `qtd_mensagens` (int, opcional): Quantidade de mensagens a manter. Padrão: 20

**Retorno:**

Lista de mensagens filtrada, removendo:
- Mensagens antigas (mantém apenas as N mais recentes)
- Mensagens de ferramenta (`role: "tool"`) no início
- Mensagens vazias no início
- Mensagens de assistente com `tool_calls` no início

---

### whatsapp_humanizer

Quebra uma mensagem em partes menores de forma inteligente para simular comportamento humano no WhatsApp.

```python
from passabot_utils import whatsapp_humanizer

# Mensagem longa
mensagem = """Olá! Aqui estão as informações:

Voos disponíveis:
- Voo 1: R$ 450,00
- Voo 2: R$ 520,00
- Voo 3: R$ 380,00

Qual você prefere?"""

# Quebra em múltiplas mensagens
partes = whatsapp_humanizer(mensagem, max_linhas_por_parte=3)

# Enviar cada parte sequencialmente
for parte in partes:
    enviar_mensagem(parte)
```

**Parâmetros:**
- `texto` (str): Mensagem completa para quebrar
- `max_linhas_por_parte` (int, opcional): Máximo de linhas por mensagem. Padrão: 3

**Retorno:**

Lista de strings (mensagens) para enviar sequencialmente.

**Comportamento:**
- Respeita quebras lógicas (cabeçalhos, listas, parágrafos)
- Agrupa cabeçalhos com seu conteúdo
- Remove links em formato markdown `[url](url)`
- Mantém formatação de listas e numerações
- Simula envio humano com mensagens menores

---

### links_markdown

Remove formatação markdown de links, mantendo apenas a URL.

```python
from passabot_utils import links_markdown

texto = "Confira: [https://exemplo.com](https://exemplo.com)"
resultado = links_markdown(texto)
# Resultado: "Confira: https://exemplo.com"
```

**Parâmetros:**
- `text` (str): Texto com links em formato markdown

**Retorno:**

Texto com links sem formatação markdown.

## Desenvolvimento

### Estrutura do projeto

```
passabot-utils/
├── passabot_utils/
│   ├── __init__.py
│   ├── message_trimmer.py
│   └── whatsapp_humanizer.py
├── setup.py
├── pyproject.toml
├── LICENSE
└── README.md
```


## 📜 License

This project is licensed under the Apache License 2.0.

You are free to use, modify, and distribute this software, including for commercial purposes, provided that you include the original copyright and license notice.

See the [LICENSE](LICENSE) file for more details.



