import re
from typing import List

def links_markdown(text: str) -> str:
    return re.sub(r'\[(https?://[^\]]+)\]\(\1\)', r'\1',text)


def whatsapp_humanizer(texto: str, max_linhas_por_parte: int = 3) -> List[str]:
    """
    Quebra uma mensagem em partes menores de forma inteligente para simular
    comportamento humano no WhatsApp. Se a mensagem contiver ':', não quebra.
    
    Args:
        texto: Mensagem completa para quebrar
        max_linhas_por_parte: Máximo de linhas por mensagem (padrão: 3)
    
    Returns:
        Lista de mensagens para enviar sequencialmente
    """
    # Se a mensagem tiver dois pontos, geralmente é um resumo ou lista, melhor não quebrar


    # Remove espaços extras
    texto = texto.strip()
    texto = links_markdown(texto)

    
    # Divide em blocos lógicos
    blocos = []
    linhas = texto.split('\n')


    
    bloco_atual = []
    
    for i, linha in enumerate(linhas):
        linha = linha.strip()
        
        # Pula linhas vazias
        if not linha:
            if bloco_atual:
                blocos.append('\n'.join(bloco_atual))
                bloco_atual = []
            continue
        
        # Identifica se é um cabeçalho ou item de lista
        eh_cabecalho = linha.endswith(':') and len(linha) < 50
        eh_item_lista = re.match(r'^[\*\-•]\s+', linha) or re.match(r'^\d+[\.\)]\s+', linha)
        
        # Se é cabeçalho e já tem conteúdo no bloco, finaliza o bloco anterior
        if eh_cabecalho and bloco_atual:
            blocos.append('\n'.join(bloco_atual))
            bloco_atual = [linha]
        # Se é item de lista, continua agrupando
        elif eh_item_lista:
            bloco_atual.append(linha)
            # Quebra se atingiu o limite de linhas
            if len(bloco_atual) >= max_linhas_por_parte:
                blocos.append('\n'.join(bloco_atual))
                bloco_atual = []
        # Linha normal
        else:
            bloco_atual.append(linha)
            # Quebra se atingiu o limite
            if len(bloco_atual) >= max_linhas_por_parte:
                blocos.append('\n'.join(bloco_atual))
                bloco_atual = []
    
    # Adiciona o último bloco se houver
    if bloco_atual:
        blocos.append('\n'.join(bloco_atual))
    
    # Otimiza blocos muito pequenos (junta cabeçalhos sozinhos com o próximo bloco)
    blocos_otimizados = []
    i = 0
    while i < len(blocos):
        bloco = blocos[i]
        
        # Se é um cabeçalho sozinho e tem próximo bloco, junta
        if bloco.endswith(':') and i + 1 < len(blocos):
            proximo = blocos[i + 1]
            blocos_otimizados.append(f"{bloco}\n{proximo}")
            i += 2
        else:
            blocos_otimizados.append(bloco)
            i += 1
    
    return blocos_otimizados


