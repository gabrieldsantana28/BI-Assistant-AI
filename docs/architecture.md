# Arquitetura

## Arquitetura utilizada

A aplicação segue uma arquitetura em camadas (Layered Architecture), separando as responsabilidades entre os diferentes módulos.

Estrutura:

Router
↓
Service
↓
OpenAI API

Os Schemas são responsáveis pela validação dos dados enviados e recebidos pela API.

Objetivos da arquitetura:

- baixo acoplamento
- alta organização
- facilidade de manutenção
- reutilização de código