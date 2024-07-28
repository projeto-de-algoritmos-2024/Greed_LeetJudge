class Solution(object):
    def minNumberOperations(self, target):
        # A operação inicial é o valor do primeiro elemento do array target
        operations = target[0]
        
        # Itera sobre o array target a partir do segundo elemento
        for i in range(1, len(target)):
            # Se o valor atual for maior que o valor anterior, precisamos fazer operações adicionais
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
        
        return operations

