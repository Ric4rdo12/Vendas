# 🛒 Vendas

Sistema de registro de vendas desenvolvido em Python, com persistência de dados em JSON.

## 📋 Funcionalidades

- ➕ **Adicionar venda** — registra nome do produto, preço e forma de pagamento
- ❌ **Remover venda** — remove uma venda pelo número da posição
- ✏️ **Editar venda** — edita nome, preço ou forma de pagamento de uma venda existente
- 🔍 **Buscar venda** — busca vendas pelo nome do produto
- 🗑️ **Limpar vendas** — apaga todas as vendas registradas
- 📊 **Ver vendas** — exibe relatório completo com totais por forma de pagamento e ranking de produtos

## 🚀 Como rodar

**Pré-requisitos:** Python instalado na máquina.

**1. Clone o repositório:**
```bash
git clone https://github.com/Ric4rdo12/Vendas.git
```

**2. Entre na pasta do projeto:**
```bash
cd Vendas
```

**3. Rode o arquivo principal:**
```bash
python Vendas2.0.py
```

## 🛠️ Tecnologias utilizadas

- Python
- JSON

## 📁 Estrutura do projeto

```
Vendas/
├── Vendas2.0.py                  # Arquivo principal
├── vendas.json                   # Dados das vendas (gerado automaticamente)
└── funcoes/
    ├── operacoes/
    │   └── modificadores.py      # Funções de adicionar, remover, editar e limpar vendas
    └── tela/
        └── visualizacao.py       # Funções de menu e visualização
```

## 👨‍💻 Autor

Ricardo — [GitHub](https://github.com/Ric4rdo12)
