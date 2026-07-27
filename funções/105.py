def notas(*n, sit =False):
    """
    -> função para analisar notas e situações de alunos
    :param n: uma ou mais notas
    :param sit: valor opcional, indica a situação do aluno
    :return: dicionário com várias informações sobre a situação da turma

    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'boa'
        elif r['média'] >=5:
            r['situação'] = 'média'
        else:
            r['situação'] = 'ruim'
    return r




resp = notas(5.2,2.7,7.9, sit=True)
print(resp)
