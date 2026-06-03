# a) Ao final desse processo, a lista está completamente ordenada? Porque?

# RESPOSTA: Sim, a lista estará totalmente ordenada. 
# Esse método segue a mesma lógica do algoritmo de Stooge Sort:
# 1. O primeiro passo ordena os primeiros 2n/3 elementos. Isso garante que os 
#    maiores elementos dessa fração sejam empurrados o máximo possível para a direita.
# 2. O segundo passo ordena os últimos 2n/3 elementos (do índice n/3 até n). Isso 
#    faz com que os maiores elementos de toda a lista fiquem definitivamente 
#    alocados no terço final (da posição 2n/3 até n).
# 3. O terceiro passo ordena novamente os primeiros 2n/3 elementos, organizando
#    o restante dos valores que ficaram para trás nas duas primeiras partes.
# Como o algoritmo da bolha ordena perfeitamente cada pedaço trabalhado, a 
# combinação dessas três etapas força toda a lista a ficar ordenada.

# b) Analise o tempo de execução desse procedimento.

# RESPOSTA: O tempo de execução será O(n²).

# JUSTIFICATIVA:
# O algoritmo realiza 3 chamadas independentes e consecutivas da função Bolha.
# Cada chamada opera em uma sublista de tamanho exatamente igual a (2n / 3).
# Sabemos que o algoritmo da bolha possui complexidade quadrática, ou seja, 
# para um tamanho 'm', seu custo é O(m²). Substituindo m = 2n/3, temos:
# Custo de 1 chamada = (2n / 3)² = (4 / 9) * n²
# Como são feitas 3 chamadas consecutivas, o custo total de tempo T(n) será:
# T(n) = 3 * [ (4 / 9) * n² ]
# T(n) = (12 / 9) * n² 
# T(n) = (4 / 3) * n²
# Desprezando as constantes multiplicativas para a análise,
# o termo dominante continua sendo n². Portanto, o tempo total é O(n²).

print("")