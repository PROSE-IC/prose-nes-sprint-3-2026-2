# PROSE NES 2026/2 - Sprint 3

Dashboard por equipe para as devolutivas do Survey Alunos. Publicacao inicial do T2 em 16/11/2026.

| Equipe | Projeto | Supervisora | Periodo | Respostas Sprint 3 |
| --- | --- | --- | --- | --- |
| T2 | Prontuario Eletronico da Psicologia | Vanessa | Vespertino | 4/6 (66,7%) |

A contagem representa quatro envios classificados, um nominal e tres com pseudonimo de equipe. Nao constitui verificacao de quatro identidades individuais distintas.

## Streamlit Community Cloud

Selecionar este repositorio, branch `main`, e a entrada `teams/t2/app.py`.

Para executar localmente:

```powershell
pip install -r requirements.txt
streamlit run teams/t2/app.py
```

## Historico E Estrutura

- `common/dashboard_app.py`: motor compartilhado, preservado da Sprint 2.
- `teams/t2/app.py`: entrada independente do T2.
- `teams/t2/data/relatos/`: relatos agregados das Sprints 0, 1 e 3.
- `docs/metodologia-dashboard.md`: criterios de calculo e interpretacao.
- `tests/test_dashboard.py`: testes de escopo, valores e filtros.

Os relatos das Sprints 0 e 1 foram preservados sem recalculo. Os dados da Sprint 2 do T2 nao estavam disponiveis nas publicacoes anteriores consultadas. Essa ausencia nao significa zero respostas e nao foi preenchida por suposicao.

Outras equipes podem ser acrescentadas mantendo `teams/tX/app.py` e seus relatos agregados em `teams/tX/data/relatos/`. A comparacao contextual exige ao menos duas equipes na mesma sprint; apenas o T2 esta publicado nesta entrega.

## Calculo E Privacidade

Mesmo schema das publicacoes anteriores: escalas reais, inversao de itens negativos, nota geral ponderada pelos blocos de perguntas e agregacao SPACE. Nota do Survey e Media SPACE filtrada sao medidas distintas. Activity nao e calculada pelo survey.

Vazios e "Prefiro nao responder" sao ausencias, nao zeros. Bases parciais sao indicadas nos itens destacados quando aplicavel. A pergunta de participacao nas discussoes usa quatro alternativas ordinais.

Somente codigo e relatos agregados sao publicados. Planilha, nomes de estudantes, respostas abertas, auditorias nominais e JSONs privados de processamento nao fazem parte do repositorio. Esta publicacao nao cria automaticamente um deployment no Streamlit Cloud.

## Testes

```powershell
python -m unittest discover -s tests -v
```
