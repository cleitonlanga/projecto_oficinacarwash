from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM", "Trocar válvula do motor"
    TROCAR_OLEO = 'TO', "Trocar óleo"
    BALACEAMENTO = 'B', "Balaceamento"
    VERIFICACAO_E_TROCA_FLUIDOS = 'VTF', "Verificação e troca de fluidos"
    TROCA_DE_CORREIA = 'TC', "Troca de correias"
    TROCA_VELAS = 'TV', "Troca de velas de ignição"
    TROCA_PASTILHAS_E_DISCO = 'TPV', "Troca de pastilhas e discos de travão"
    TROCA_PNEUS = 'TP', "Troca de pneus"
