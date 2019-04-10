from mcpi.minecraft import  Minecraft
import mcpi.block as block
import random
mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)
def housebuild(size,initalpos_x,initalpos_y,initalpos_z):
    if size=="S":
        for b in range(4):
            for a in range(4):
                mc.setBlock(initalpos_x+3+b, initalpos_y, initalpos_z+a, 1)
        for b in range(4):
            for a in range(4):
                mc.setBlock(initalpos_x+3+b, initalpos_y+3, initalpos_z+a, 1)
        for a in range(2):
            mc.setBlock(initalpos_x+3, initalpos_y+1+a, initalpos_z,1)
            mc.setBlock(initalpos_x+6, initalpos_y+1+a, initalpos_z,1)
            mc.setBlock(initalpos_x+3, initalpos_y+1+a, initalpos_z+3,1)
            mc.setBlock(initalpos_x+6, initalpos_y+1+a, initalpos_z+3,1)
        for a in range(4):
            mc.setBlock(initalpos_x+3+a, initalpos_y+1, initalpos_z,1)
            mc.setBlock(initalpos_x+3+a, initalpos_y+1, initalpos_z+3,1)
            mc.setBlock(initalpos_x+6, initalpos_y+1, initalpos_z+a,1)
    elif size=="M":
        for b in range(6):
            for a in range(6):
                mc.setBlock(initalpos_x+3+b, initalpos_y, initalpos_z+a, 1)
        for b in range(6):
            for a in range(6):
                mc.setBlock(initalpos_x+3+b, initalpos_y+5, initalpos_z+a, 1)
        for a in range(4):
            mc.setBlock(initalpos_x+3, initalpos_y+1+a, initalpos_z,1)
            mc.setBlock(initalpos_x+8, initalpos_y+1+a, initalpos_z,1)
            mc.setBlock(initalpos_x+3, initalpos_y+1+a, initalpos_z+5,1)
            mc.setBlock(initalpos_x+8, initalpos_y+1+a, initalpos_z+5,1)
        for a in range(6):
            mc.setBlock(initalpos_x+3+a, initalpos_y+1, initalpos_z,1)
            mc.setBlock(initalpos_x+3+a, initalpos_y+1, initalpos_z+5,1)
            mc.setBlock(initalpos_x+8, initalpos_y+1, initalpos_z+a,1)
    else:
        size=int(size)
        for b in range(size):
            for a in range(size):
                mc.setBlock(initalpos_x+3+b, initalpos_y, initalpos_z+a, 1)
        for b in range(size):
            for a in range(size):
                mc.setBlock(initalpos_x+3+b, initalpos_y+size, initalpos_z+a, 1)
        for a in range(size-1):
            mc.setBlock(initalpos_x+3, initalpos_y+1+a, initalpos_z,1)
            mc.setBlock(initalpos_x+2+size, initalpos_y+1+a, initalpos_z,1)
            mc.setBlock(initalpos_x+3, initalpos_y+1+a, initalpos_z+size-1,1)
            mc.setBlock(initalpos_x+2+size, initalpos_y+1+a, initalpos_z+size-1,1)
        for a in range(size):
            mc.setBlock(initalpos_x+3+a, initalpos_y+1, initalpos_z,1)
            mc.setBlock(initalpos_x+3+a, initalpos_y+1, initalpos_z+size-1,1)
            mc.setBlock(initalpos_x+2+size, initalpos_y+1, initalpos_z+a,1)
    return True

pos = mc.player.getTilePos()
print(pos.x,pos.y,pos.z)
x1=pos.x
y1=pos.y
z1=pos.z
for i in range(3):
    for j in range(3):
        for k in range(3):
            housebuild(random.randint(4,11),x1,y1,z1)
            x1=x1+14
        x1= pos.x
        z1=z1+14
    z1= pos.z
    y1=y1+14
    
print("Finished")
        
            

