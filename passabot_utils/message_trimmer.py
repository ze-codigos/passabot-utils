"""
Módulo para trimming de mensagens em conversações de agentes.
"""

from typing import List, Optional, Dict
from pydantic import BaseModel

class Messages(BaseModel):
    role: str
    content: str
    tool_calls: Optional[List[Dict]] = None
    tool_call_id: Optional[str] = None


def trim_messages(messages: List[Messages], qtd_mensagens: Optional[int] = 20) -> List[Messages]:
    """
    Remove mensagens antigas e problemáticas mantendo apenas as mais recentes.
    
    Args:
        messages: Lista de mensagens da conversa
        qtd_mensagens: Quantidade de mensagens a manter (padrão: 20)
    
    Returns:
        Lista de mensagens filtrada
    
    Examples:
        >>> messages = [{"role": "user", "content": "oi"}]
        >>> trimmed = trim_messages(messages, qtd_mensagens=10)
    """
    # Se tem qtd_mensagens ou menos, retorna todas
    if len(messages) <= qtd_mensagens:
        return messages
    
    # Pega as últimas qtd_mensagens
    messages_trimmed = messages[-qtd_mensagens:]
    
    # Remove mensagens problemáticas do início
    while messages_trimmed and (
        messages_trimmed[0].get("role") == "tool" or 
        (messages_trimmed[0].get("content") == "" and messages_trimmed[0].get("role") != "tool") or 
        (messages_trimmed[0].get("role") == "assistant" and 
         messages_trimmed[0].get("content") != "" and 
         messages_trimmed[0].get("tool_calls"))
    ):
        messages_trimmed = messages_trimmed[1:]
    
    return messages_trimmed

