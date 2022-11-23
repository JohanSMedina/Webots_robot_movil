import numpy
npmatlab = [1,1],[2,1],[2,3],[5,3],[5,2],[6,2],[6,1],[10,1],[10,3]
nuevaPosicion = npmatlab

for i in range(len(npmatlab)):
    print(nuevaPosicion[i])
    nuevaPosicion[i][0] = round(nuevaPosicion[i][0] * 0.2 - 0.1,1)
    nuevaPosicion[i][1] = round(nuevaPosicion[i][1] * 0.2 - 0.1,1)
    print(nuevaPosicion[i][0])
    print(nuevaPosicion[i][1])

for i in range(len(npmatlab)):
    print(nuevaPosicion[i])

PosQuerida = nuevaPosicion[1]
posx = PosQuerida[0]
posy = PosQuerida[1]
print(f"Pos X: {posx}, Pos Y: {posy}")