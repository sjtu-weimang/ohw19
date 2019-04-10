from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import time

#请自行修改服务器的ip地址
mc=Minecraft.create("192.168.2.207",4711)

poss=[]

#4个玩家的初始基地位置
poss.append(Vec3(48,0,20))
poss.append(Vec3(105,-1,47))
poss.append(Vec3(107,6,121))
poss.append(Vec3(63,8,123))

#先巡视一下所有基地
for pos in poss:
    mc.player.setTilePos(pos)
    time.sleep(2)

stayed_time=0

while True:
    stayed_time+=1
    print("xkn stay_time"+str(stayed_time))
    time.sleep(2)
    #建造带火把的通天柱子为每个玩家标定位置，玩家编号为柱子中的连续石块的数字，为防止被破坏，每3秒恢复一次
    for idx,pos in enumerate(poss):
        for y in range(50):
            mc.setBlock(pos.x,pos.y+y,pos.z,1 if y%(idx+1) else 2)
            mc.setBlock(pos.x+1,pos.y+y,pos.z,50)
    #通过宝剑右敲击产生事件从而定位不同玩家位置，face为被敲击的石块的6个面的编号，id貌似是玩家编号
    hits=mc.events.pollBlockHits() 
    for hit in hits:
        mc.postToChat("Hit:"+"x"+str(hit.pos.x)+"y"+str(hit.pos.y)+"z"+str(hit.pos.z)+"f"+str(hit.face)+"     id:"+str(hit.entityId))
