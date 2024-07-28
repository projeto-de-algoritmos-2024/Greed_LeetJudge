class Solution(object):
    def findMinArrowShots(self, points):

        # Ordenar os pontos pelo ponto final (xend)
        points.sort(key=lambda x:x[1]) 

        arrowsCount = 1
        end = points[0][1] # Ponto final do primeiro balão

        for i in range(1, len(points)):
            # Se o ponto inicial do balão atual está além do ponto final do balão anterior
            if points[i][0] > end: 
                arrowsCount += 1
                end = points[i][1]

        return arrowsCount