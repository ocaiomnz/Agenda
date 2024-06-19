from datetime import datetime, timedelta

# Função para criar os blocos de 30 minutos
def criar_blocos():
    blocos = {}
    inicio = datetime.strptime("00:00", "%H:%M")
    for i in range(48):  # 24 horas * 2 blocos por hora = 48 blocos
        bloco_inicio = inicio + timedelta(minutes=30 * i)
        bloco_fim = bloco_inicio + timedelta(minutes=30)
        blocos[bloco_inicio.strftime("%H:%M")] = None
    return blocos

# Função para verificar disponibilidade
def verificar_disponibilidade(blocos, horario):
    return blocos.get(horario) is None

# Função para alocar horário
def alocar_horario(blocos, nome, horario):
    if verificar_disponibilidade(blocos, horario):
        blocos[horario] = nome
        return True
    return False

# Função para cancelar alocação
def cancelar_alocacao(blocos, horario):
    if blocos.get(horario) is not None:
        blocos[horario] = None
        return True
    return False

# Função para mostrar blocos disponíveis
def mostrar_blocos_disponiveis(blocos):
    return [horario for horario, usuario in blocos.items() if usuario is None]
