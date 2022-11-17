from PIL import Image, ImageDraw
with Image.open("img.png") as im1:
    with Image.open("img1.png") as im2:
        max_size = (max(im1.width, im2.width), max(im1.height, im2.height))
        imA = Image.new("RGB", max_size)
        imA.paste(im1.convert("RGB"))
        imB = Image.new("RGB", max_size)
        imB.paste(im2.convert("RGB"))
pxA = imA.load()
pxB = imB.load()
outlined = []
rects = []
d = ImageDraw.Draw(imB)
for x in range(max_size[0]):
    for y in range(max_size[1]):
        if (x, y) in outlined or pxA[x, y] == pxB[x, y]:
            continue
    
        w, h = 10, 20
        overlap = False
        for a in range(w):
            for b in range(h):
                point = (x+a, y+b)
                if point in outlined:
                    overlap = True
                    break
                outlined.append(point)
            if overlap:
                break
        if overlap:
            continue
        rects.append((x, y, x+w, y+h))
for rect in rects:
    d.rectangle(rect, outline="#f00")
imB.save("out.png")