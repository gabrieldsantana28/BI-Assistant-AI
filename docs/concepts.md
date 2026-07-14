# Conceitos Importantes

## Separação de Responsabilidades (Separation of Concerns)

Cada módulo do sistema deve possuir apenas uma responsabilidade bem definida.

No BI Assistant AI:

- Router → recebe requisições HTTP.
- Service → executa a lógica de negócio.
- Schema → valida os dados.
- Prompt → define o comportamento da IA.

Essa separação reduz o acoplamento e facilita a manutenção do projeto.

---

## Configuração vs Código

Código é composto por algoritmos e regras de execução.

Configuração altera o comportamento da aplicação sem modificar sua lógica.

Exemplo:

- Código: funções Python, condicionais e laços.
- Configuração: `.env`, `system_prompt.txt`, `requirements.txt`.

## Cache em Memória

Uma aplicação pode carregar configurações ou arquivos apenas uma vez durante sua inicialização, mantendo-os em memória para evitar leituras repetidas em disco. Essa técnica melhora o desempenho e reduz operações de I/O.

## Coesão

Manter funções e classes próximas do contexto onde são utilizadas.

Exemplo:
load_system_prompt() pertence ao AIService e não à pasta utils.

## Tratamento de Exceções

Utilização de try/except para impedir que erros inesperados interrompam a execução da aplicação.

## Raise

Interrompe imediatamente a execução de uma função lançando uma exceção.

## Return

Finaliza a função devolvendo um valor ao código que a chamou.

## Arquitetura Escalável

Uma arquitetura deve permitir que novas funcionalidades sejam adicionadas sem exigir grandes alterações no código existente.

Exemplo:
Adicionar um novo provedor de IA criando um novo Service, sem modificar os já existentes.