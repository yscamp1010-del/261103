boxes = []
for i in range(-4, 4) : 
    for j in range(-4,4) : 
        boxes.append(box(pos = vec(i,j,0), size = vec(0.9,0.9,0.1)))




while True :
    rate(100)
    k = keysdown()
    if 'right' in k :
        boxes[i].color = color.red
