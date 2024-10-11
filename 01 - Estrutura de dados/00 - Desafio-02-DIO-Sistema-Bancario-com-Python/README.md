![DIO](https://img.shields.io/badge/DIO-FF9900?style=for-the-badge&logo=dio&logoColor=white) ![Bootcamp](https://img.shields.io/badge/Bootcamp-4B8BBE?style=for-the-badge&logo=bootstrap&logoColor=white) ![Engenharia](https://img.shields.io/badge/Engenharia-4B8BBE?style=for-the-badge&logo=engineering&logoColor=white) ![Dados](https://img.shields.io/badge/Dados-00A3E0?style=for-the-badge&logo=data&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Engenharia de Dados com Python](https://img.shields.io/badge/Engenharia%20de%20Dados%20com%20Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Sistema Bancário](https://img.shields.io/badge/Sistema%20Bancário-30A3DC?style=for-the-badge&logo=bank&logoColor=white)

💵 :bank:  Desafio-02-Sistema-Bancário-com-Python-V2. :bank: 💵

Com os novos conhecimentos adquiridos sobre data e hora, você foi encarregado de implementar as seguintes funcionalidades no sistema do Desafio-01:

# **Funcionalidades**

**Limite de Transações:** Estabelecer um limite de 10 transações diárias para uma conta.

**Notificação de Limite Excedido:** Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado de que excedeu o número de transações permitidas 
para aquele dia.

**Extrato:** Mostrar no extrato a data e hora de todas as transações.

# **Objetivo Geral**

*Separar as funções existentes de saque, depósito e extrato em funções distintas.* 

**Criar duas novas funções:** cadastrar usuário (cliente) e cadastrar conta bancária.

Precisamos modularizar o código. Para isso, vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato. 

Além disso, para a versão 2 do nosso sistema, precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com o usuário).

# **Funções a Serem Criadas**

**Função Saque:**

Deve receber os argumentos apenas por nome (keyword only).

**Sugestão de argumentos:** saldo, valor, extrato, limite, numero_saques, limite_saques.

**Sugestão de retorno:** saldo e extrato.

# **Função Depósito:**

Deve receber os argumentos apenas por posição (positional only).

**Sugestão de argumentos:** saldo, valor, extrato.

**Sugestão de retorno:** saldo e extrato.

# **Função Extrato:**

Deve receber os argumentos tanto por posição quanto por nome (positional only e keyword only).

**Argumentos posicionais:** saldo.

**Argumentos nomeados:** extrato.

# **Novas Funções**

Precisamos criar duas novas funções: criar usuário e criar conta corrente. **Sinta-se à vontade para adicionar mais funções, como por exemplo: listar contas.**

# **Criar Usuários (Cliente)**

O programa deve armazenar os usuários em uma lista. 

**Um usuário é composto por:** nome, data de nascimento, CPF e endereço. 

**O endereço deve ser uma string no formato:** logradouro, número - bairro - cidade/sigla estado. 

Devemos armazenar apenas os números do CPF e não podemos cadastrar dois usuários com o mesmo CPF.

O programa também deve armazenar contas em uma lista. 

**Uma conta é composta por:** agência e número da conta. 

O número da conta é sequencial, começando em 1, enquanto o número da agência é fixo: "0001". 

O usuário pode ter mais de uma conta, mas cada conta pertence a apenas um usuário.

# **Dica**

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número de CPF ##informado para cada usuário da lista.
