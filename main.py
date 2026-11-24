Web VPython 3.2
print("Blue = 1")
print("red = land mine")




box(pos = vec(0,0,-0.05), size = vec(0.8,0.8,0.1), color = color.red)
box(pos = vec(0,1,-0.05), size = vec(0.8,0.8,0.1), color = color.blue)
box(pos = vec(-1,1,-0.05), size = vec(0.8,0.8,0.1), color = color.blue)
box(pos = vec(0,-1,-0.05), size = vec(0.8,0.8,0.1), color = color.blue)
box(pos = vec(-1,0,-0.05), size = vec(0.8,0.8,0.1), color = color.blue)

box(pos = vec(1,1,-0.05), size = vec(0.8,0.8,0.1), color = color.blue)
box(pos = vec(1,0,-0.05), size = vec(0.8,0.8,0.1), color = color.blue)
box(pos = vec(0,1,-0.05), size = vec(0.8,0.8,0.1), color = color.blue)
box(pos = vec(-1,-1,-0.05), size = vec(0.8,0.8,0.1), color = color.blue)
box(pos = vec(1,-1,-0.05), size = vec(0.8,0.8,0.1), color = color.blue)

boxes = []
for i in range(-4, 4) : 
    for j in range(-4,4) : 
        
        boxes.append(box(pos = vec(i,j,-0.1), size = vec(0.8,0.8,0.1)))

# 열린판 리스트
boxes = []
for i in range(-4, 4) : 
    for j in range(-4,4) : 
        
        boxes.append(box(pos = vec(i,j,0), size = vec(0.9,0.9,0.1)))

# 마우스 클릭
def on_click(evt):
    hit = scene.mouse.pick
    if hit:
        hit.opacity = 0 # 마우스 색 변경

scene.bind('click',on_click)



