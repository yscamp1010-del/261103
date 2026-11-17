box((pos = vec(0,0,-0.1), size = vec(0.9,0.9,0.1), color = color(0,0,0))


# 가람판 리스트

boxes = []
for i in range(-4, 4) : 
    for j in range(-4,4) : 
        
        boxes.append(box(pos = vec(i,j,-0.1), size = vec(0.9,0.9,0.1)))



# 열린판 리스트
boxes = []
for i in range(-4, 4) : 
    for j in range(-4,4) : 
        
        boxes.append(box(pos = vec(i,j,0), size = vec(0.9,0.9,0.1)))

# 마우스 클릭
def on_click(evt):
    hit = scene.mouse.pick
    if hit:
        hit.color = color.red  # 마우스 색 변경

scene.bind('click',on_click)

