from ninja import Router
from ninja.errors import HttpError
from .schemas import AlunosSchema, ProgressoAlunoSchema, AulaRealizadaSchema
from .models import Alunos, AulasConcluidas
from typing import List
from .graduacao import *
from datetime import date

treino_router = Router()

@treino_router.post('/', response={200: AlunosSchema})
def criar_aluno(request, aluno_schema: AlunosSchema):
    nome = aluno_schema.dict()['nome']
    email = aluno_schema.dict()['email']
    faixa = aluno_schema.dict()['faixa']
    data_nascimento = aluno_schema.dict()['data_nascimento']

    if Alunos.objects.filter(email=email).exists():
        raise HttpError(400, "E-mail já cadastrado.")

    aluno = Alunos(nome=nome, email=email, faixa=faixa, data_nascimento=data_nascimento)
    aluno.save()
    
    return aluno


@treino_router.get('/alunos/', response=List[AlunosSchema])
def listar_alunos(request):
    alunos = Alunos.objects.all()
    return alunos


@treino_router.get('/progresso_aluno/', response={200: ProgressoAlunoSchema})
def progresso_aluno(request, email_aluno: str):
    aluno = Alunos.objects.get(email=email_aluno)
    
    total_aulas_concluidas = AulasConcluidas.objects.filter(aluno=aluno).count()
    
    faixa_atual = aluno.get_faixa_display()
    
    n = order_belt.get(faixa_atual, 0)
  
    total_aulas_proxima_faixa = calculate_lessons_to_upgrade(n)

    total_aulas_concluidas_faixa = AulasConcluidas.objects.filter(aluno=aluno, faixa_atual=aluno.faixa).count()

    aulas_faltantes = max(total_aulas_proxima_faixa - total_aulas_concluidas_faixa, 0)

    return {
        "email": aluno.email,
        "nome": aluno.nome,
        "faixa": aluno.get_faixa_display(),
        "total_aulas": total_aulas_concluidas,
        "aulas_necessarias_para_proxima_faixa": aulas_faltantes
    }

@treino_router.post('/aula_realizada/', response={200: str})
def aula_realizada(request, aula_realizada: AulaRealizadaSchema):
    qtd = aula_realizada.dict()['qtd']
    email_aluno = aula_realizada.dict()['email_aluno']

    if qtd <= 0:
        raise HttpError(400, "Quantidade de aulas realizadas inválida.")

    aluno = Alunos.objects.get(email=email_aluno)

    aulas = [
        AulasConcluidas(aluno=aluno, faixa_atual=aluno.faixa)
        for _ in range(qtd)
    ]

    AulasConcluidas.objects.bulk_create(aulas)

    return 200, f"Aulas Cadastradas com sucesso."



@treino_router.put("/alunos/{aluno_id}", response=AlunosSchema)
def update_aluno(request, aluno_id: int, aluno_data: AlunosSchema):
    aluno = Alunos.objects.get(id=aluno_id)
    
    idade = date.today() - aluno.data_nascimento

    if int(idade.days/365) < 18 and aluno_data.dict()['faixa'] in ('A', 'R', 'M', 'P'):
        raise HttpError(400, "O aluno é menor de idade e não pode ser graduado para essa faixa.")

    #exclude_unset=True
    for attr, value in aluno_data.dict().items():
        if value:
            setattr(aluno, attr, value)
    
    aluno.save()
    return aluno