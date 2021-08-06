from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.fields import IntegerField
#precisa definir quais campos podem ficar em branco e quais são obrigatorios t
#revisar se está tudo certo tanto nos tamanhos quanto no tipo de var
#tem um campo quec é um if (como faz ?)

estrutura_CHOICE = (
    ('1','Coleção'),
    ('2','Misturado'),
    ('3','Linear'),
    ('4','Hierárquico'), 
    ('5','Em rede'), 
    ('6','Ramificado'),   
    ('7','Parcelado'), 
    ('8','Atômico'), 
)

nivel_de_agregacao_CHOICE = (
    ('1','Menor nivel de agregação'),
    ('2','Coleção de agregação'),
    ('3', 'a collection of level 2 learning objects'),
    ('4','the largest level of granularity'),   
)

status_CHOICE = (
    ('1','Rascunho'),
    ('2','Final'),
    ('3','Revisado'),
    ('4','Indisponivel'),   
)

papel_CHOICE = (
    ('1','Autor'),
    ('2','Editor'),
    ('3','Iniciador'),
    ('4','Terminator'),
    ('5','Validador'),   
    ('6','Editor'), 
    ('7','Designer Gráfico'), 
    ('8','Implementador Técnico'), 
    ('9','Provedor de conteúdos'), 
    ('10','Validador Técnico'), 
    ('11','Validador Educacional'), 
    ('12','Roteirista'), 
    ('13','Designer instrucional'), 
)
tipo_CHOICE = (
    ('OP','Operating System'),
    ('BW','Browser'),  
)
nome_OP_CHOICE = (
    ('1','PC_DOS'),
    ('2','MS-Windows'),
    ('3','MacOS'),
    ('4','Unix'), 
    ('5','Multi-OS'),  
    ('6','Nenhum'),    
)
nome_Browser_CHOICE = (
    ('1','Netscape'),
    ('2','Communicator'),
    ('3','Microsoft'),
    ('4','Internet Explorer'), 
    ('5','Opera'),  
    ('6','Amaya'),    
)
tipo_de_Interatividade_CHOICE = (
    ('1','Ativo'),
    ('2','Expositivo'),
    ('3','Misturado'),
    ('4','Indefinido'), 
)
tipo_de_recurso_de_aprendizagem_CHOICE = (
    ('1','Exercício'),
    ('2','Simulação'),
    ('3','Questionário'),
    ('4','Diagrama'),
    ('5','Figura'),   
    ('6','Gráfico'), 
    ('7','Índice'), 
    ('8','Slide'), 
    ('9','Tabela'), 
    ('10','Texto narrativo'), 
    ('11','Exame'), 
    ('12','Experimentar'), 
    ('13','Declaração do Problema'),
    ('14','Auto-avaliação'),
)
nivel_CHOICE = (
    ('1','muito baixo'),
    ('2','baixo'),
    ('3','médio'),
    ('4','Alto'), 
    ('5','muito alto'),
)
usuario_final_CHOICE = (
    ('1','Professora'),
    ('2','Autor'),
    ('3','Aprendiz'),
    ('4','Gerente'), 
)
contexto_de_aprendizagem_CHOICE = (
    ('1','Educação primária'),
    ('2','Educação secundária'),
    ('3','Ensino superior'),
    ('4','Ensino superior'), 
    ('5','Primeiro Ciclo Universitário'),  
    ('6','Segundo Ciclo Universitário'),
    ('7','Pôs Graduação'),
    ('8','Primeiro Ciclo Escola Técnica'), 
    ('9','Segundo Ciclo Escola Técnica'),    
    ('10','Formação Profissional'),
    ('11','Formação Contínua'),
    ('12','Trainee'),
)
finalidade_CHOICE = (
    ('1','Disciplina'),
    ('2','Idéia'),
    ('3','Pré-requisito'),
    ('4','Objetivo Educacional'), 
    ('5','Restrições de acessibilidade'),
    ('6','Nível educacional'), 
    ('7','Nível de habilidade'), 
    ('8','Nível de segurança'), 
)

class LivroArtigo(models.Model):
    geral = models.OneToOneField('Geral', on_delete=models.CASCADE)
    ciclo_de_vida = models.OneToOneField('ciclo_de_vida', on_delete=models.CASCADE)
    meta_metadados = models.OneToOneField('meta_metadados', on_delete=models.CASCADE)
    identificador = models.OneToOneField('identificador', on_delete=models.CASCADE)
    contribuinte = models.OneToOneField('contribuinte', on_delete=models.CASCADE)
    metadados_tecnicos = models.OneToOneField('metadados_tecnicos', on_delete=models.CASCADE)
    requisitos = models.OneToOneField('requisitos', on_delete=models.CASCADE)
    aspectos_Educacionais = models.OneToOneField('aspectos_Educacionais', on_delete=models.CASCADE)
    direitos = models.OneToOneField('direitos', on_delete=models.CASCADE)
    relacoes = models.OneToOneField('relacoes', on_delete=models.CASCADE)
    recurso = models.OneToOneField('recurso', on_delete=models.CASCADE)
    anotacao = models.OneToOneField('anotacao', on_delete=models.CASCADE)
    Classificacao = models.OneToOneField('Classificacao', on_delete=models.CASCADE)

    def __str__(self):
        return self.geral.titulo

class Geral(models.Model):

    titulo = models.CharField(
        'Titulo', max_length=120)
    linguagem = models.CharField(
        'Linguagem', max_length=15)
    descricao = models.CharField(
        'Descrição', max_length=150)
    palavras_chave = models.CharField(
        'Palavras Chave', max_length=50)
    cobertura = models.CharField(
        'Cobertura', max_length=15)
    estrutura = models.CharField(
        'Estrutura', max_length=20, choices=estrutura_CHOICE)
    nivel_de_agregacao = models.CharField(
        'Nivel_de_Agregação',max_length=2, choices=nivel_de_agregacao_CHOICE )

    verbose_name = 'geral'
    
    def __str__(self):
        return self.titulo
    #essa função em cima é pra nomear o objeto que a classe vai gerar, tem q escolher um pra cada uma das outras

    

class ciclo_de_vida(models.Model):
    versao = models.IntegerField(
        'Versao')
    status = models.CharField(
        'Status', max_length=15, choices=status_CHOICE)
    entidade = models.CharField(
        'Entidade', max_length=20)
    datas = models.DateField(
        'Data', blank=True, null=True)    


class meta_metadados(models.Model):
    esquema_de_metadados = models.CharField(
        'Esquema_de_Metadados', max_length=20)

class identificador(models.Model):
    catalogo = models.CharField(
        'Catalogo', max_length=150)
    entrada = models.DateField(
        'Entrada', blank=True, null=True)

class contribuinte(models.Model):
    papel = models.CharField(
        'Papel', max_length=15, choices=papel_CHOICE)
    entidade = models.CharField(
        'Entidade', max_length=20)
    data = models.DateField(
        'Data', blank=True, null=True) 

class metadados_tecnicos(models.Model):
    formato = models.CharField(
        'Formato', max_length=15)
    tamanho = models.CharField(
        'Tamanho', max_length=20)
    requisitos = models.CharField(
        'Requisitos', max_length=50)
    localizacao = models.CharField(
        'Localizacao', max_length=50)
    observacoes_de_instalacoes = models.TextField(
        'Observacoes_de_Instalacoes')
    outros_Requisitos_de_Sistema = models.TextField(
        'Outros_Requisitos_de_Sistema')
    duracao = models.DateTimeField(
        'Duracao')


class requisitos(models.Model):
    tipo = models.CharField(
        'tipo', max_length=15, choices=tipo_CHOICE)
    nome = models.CharField(
        'Nome', max_length=20, choices=nome_OP_CHOICE)#esse aqui qual lista de opções vai aparecer depende do que marcou na anterior (SO ou BW) 
    versao_min = models.CharField(
        'Versao_min', max_length=20) 
    versao_max = models.CharField(
        'Versao_max', max_length=20) 

class aspectos_Educacionais(models.Model):
    tipo_de_Interatividade = models.CharField(
        'Tipo_de_Interatividade', max_length=15, choices=tipo_de_Interatividade_CHOICE)
    tipo_de_recurso_de_aprendizagem = models.CharField(
        'Tipo_de_recurso_de_aprendizagem', max_length=20, choices=tipo_de_recurso_de_aprendizagem_CHOICE)
    nivel_de_interatividade = models.CharField(
        'Nivel_de_interatividade', max_length=20, choices=nivel_CHOICE)
    densidade_semantica = models.CharField(
        'Densidade_semântica', max_length=20, choices=nivel_CHOICE)
    usuario_final = models.CharField(
        'Usuário_final', max_length=20, choices=usuario_final_CHOICE)
    contexto_de_aprendizagem = models.CharField(
        'Contexto_de_aprendizagem', max_length=20, choices=contexto_de_aprendizagem_CHOICE)
    idade_recomendada = models.CharField(
        'Idade_Recomendada', max_length=20)
    grau_de_dificuldade = models.CharField(
        'Grau_de_dificuldade', max_length=20, choices=nivel_CHOICE)
    tempo_de_aprendizado = models.DateTimeField(
        'Tempo_de_aprendizado')
    descricao = models.CharField(
        'Descricao', max_length=100)
    linguagem = models.CharField(
        'Linguagem', max_length=20)

class direitos(models.Model):
    custo = models.FloatField(
        'Custo')
    direitos_autorais = models.CharField(
        'Direitos_autorais', max_length=20)
    descricao = models.CharField(
        'Descricao', max_length=100)

class relacoes(models.Model):
    genero = models.CharField(
        'Gênero',max_length=20)
    recurso = models.CharField(
        'Recurso', max_length=20)
    
class recurso(models.Model):
    descricao = models.CharField(
        'Descrição',max_length=20)

class anotacao(models.Model):
    pessoa = models.CharField(
        'Pessoa',max_length=20)
    data = models.DateTimeField(
        'Data')
    descricao = models.CharField(
        'Descricao', max_length=100)

class Classificacao(models.Model):
    finalidade = models.CharField(
        'finalidade', max_length=20, choices=finalidade_CHOICE)
    palavras_chave = models.CharField(
        'Palavras Chave', max_length=50)

