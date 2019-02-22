import sys
import math
from random import randint

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
zona1=[] #untuk menampung zona yang saling link
zona2=[] #untuk menampung zona yang saling link

for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]

for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    zona1 += [zone_1]
    zona2 += [zone_2]

# game loop
while True:
    my_platinum = int(input())  # your available Platinum

    zonakita, podkita, podlawan = [], [], [] # list untuk mengumpulkan data dalam loop game
    mungkingerak = [] #kemungkinan pod dalam suatu zona gerak ke zona lain ditampung disini
    count = 0

    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]

        if owner_id == my_id:
            zonakita += [z_id]
            podkita += [pods_p0]
            podlawan += [pods_p1]

            mungkingerak.append([])
            for i in range(len(zona1)):
                if zona1[i] == z_id:
                    mungkingerak[count].append(zona2[i])
                if zona2[i] == z_id:
                    mungkingerak[count].append(zona1[i])

            count += 1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # first line for movement commands, second line no longer used (see the protocol in the statement for details)
    move = []

    for i in range(len(zonakita)):
        if podkita[i] // 2 > 0 :
            podgerak = podkita[i] // 2
        else:
            podgerak=1
        cek=[] #dibawah ini untuk atur supaya pod bergerak ke zona yang bukan milik kita(netral or punya lawan)
        for a in range(len(zonakita)):
            for b in range(len(mungkingerak[i])):
                if zonakita[a]!=mungkingerak[i][b]:
                    cek+=[mungkingerak[i][b]]
        if len(cek)!=0:
            go=cek[randint(0,len(cek)-1)]
        else:
            go=mungkingerak[i][randint(0, len(mungkingerak[i]) - 1)]
        move += [podgerak, zonakita[i],go]

    for i in move:
        print(i, end = " ")
    print()
    print("WAIT")
