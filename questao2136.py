class Solution:
    def earliestFullBloom(self, plantTime, growTime):
        # Transformando em um array de intervalos
        flowers = [(plantTime[i], growTime[i]) for i in range(len(plantTime))]

        # Ordenar pelo maior growTime primeiro e em caso de empate pelo menor plantTime
        flowers.sort(key=lambda x:(-x[1], x[0]))

        maxDays = 0 
        passedDays = 0

        for plant, grow in flowers:
            passedDays += plant
            maxDays = max(maxDays, passedDays + grow)

        return maxDays