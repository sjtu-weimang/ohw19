import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

a=pos.x
b=pos.y
c=pos.z

def house(a, b ,c , L, W, H, M):
	for j in range(H):
		for i in range(W):
			if j>=1 and j<=3:
				if i>=int(W/2)-1 and i<=int(W/2):
					pass
				else:
					mc.setBlock(a+1+i, b+j, c+1, M)
			else:
				mc.setBlock(a+1+i, b+j, c+1, M)
			mc.setBlock(a+1+i, b+j, c+L, M)
			
		for k in range(L-2):
			if (k==int(L/2)-1 or k==int(L/2)-2) and (j==int(H/2) or j==int(H/2)-1):           
				pass
			else:				
				mc.setBlock(a+1, b+j, c+k+2, M)
				mc.setBlock(a+W, b+j, c+k+2, M)
	
	for i in range(W-2):                       			#底
		for k in range(L-2):
			mc.setBlock(a+2+i, b, c+2+k, M)
			
	for i in range(W-2):						#顶
		for k in range(L-2):
			mc.setBlock(a+2+i, b+H-1, c+2+k, M)
    
print([a,b,c])
house(a, b, c, 10, 10, 10, 1)
house(a+14, b, c, 10, 10, 10, 2)
house(a+28, b, c, 10, 10, 10, 3)
house(a, b, c+14, 10, 10, 10, 4)
house(a+14, b, c+14, 10, 10, 10, 133)
house(a+28, b, c+14, 10, 10, 10, 5/1)
house(a, b, c+28, 10, 10, 10, 5/2)
house(a+14, b, c+28, 10, 10, 10, 5/3)
house(a+28, b, c+28, 10, 10, 10, 7)
house(a, b+14, c, 10, 10, 10, 14)
house(a+14, b+14, c, 10, 10, 10, 15)
house(a+28, b+14, c, 10, 10, 10, 16)
house(a, b+14, c+14, 10, 10, 10, 121)
house(a+14, b+14, c+14, 10, 10, 10, 17/1)
house(a+28, b+14, c+14, 10, 10, 10, 133)
house(a, b+14, c+28, 10, 10, 10, 17/3)
house(a+14, b+14, c+28, 10, 10, 10, 21)
house(a+28, b+14, c+28, 10, 10, 10, 22)
house(a, b+28, c, 10, 10, 10, 41)
house(a+14, b+28, c, 10, 10, 10, 42)
house(a+28, b+28, c, 10, 10, 10, 45)
house(a, b+28, c+14, 10, 10, 10, 48)
house(a+14, b+28, c+14, 10, 10, 10, 49)
house(a+28, b+28, c+14, 10, 10, 10, 56)
house(a, b+28, c+28, 10, 10, 10, 57)
house(a+14, b+28, c+28, 10, 10, 10, 73)
house(a+28, b+28, c+28, 10, 10, 10, 88)
            
#origin : (189, 53, -160)
