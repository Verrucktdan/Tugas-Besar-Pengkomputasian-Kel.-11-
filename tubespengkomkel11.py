max = float('inf')
start = []
dest = []
dist = []

def panjang(list):
    index = 0
    while list!=[]:
        list = list[0:-1]
        index+=1
    return index

def init_dist(k = 0):
    init = dist
    init = [ max ] * jumlah_simpang
    init[k] = 0
    return init

def matrix_baru():
    grid = int(input("Banyak jumlah simpang: "))
    matrix = [[0 for i in range(grid)] for i in range(grid)]
    state = ""
    while (state=="" or state=="y") and state!="n":
        dari = int(input("dari titik: "))
        ke = int(input("ke titik: "))
        jarak = int(input("dengan jarak: "))
        matrix[dari-1][ke-1] = jarak
        state = input("Masih mau menginput jarak?(y/n): ")
    return grid, matrix

def rute_eff(awal, akhir):
    iid = int(awal) - 1
    fid = int(akhir) - 1
    simpang_eff = iid
    jejak = [iid]
    dist = init_dist(iid)
    alur = {}
    while panjang(jejak)<=jumlah_simpang and simpang_eff!=fid:
        for i in range(jumlah_simpang):
            if i not in jejak and adjacency_matrix[simpang_eff][i] > 0 and \
                i!=simpang_eff and dist[i]>adjacency_matrix[simpang_eff][i]:
                dist[i] = adjacency_matrix[simpang_eff][i] + dist[simpang_eff]
                alur = {**alur, **{i+1: {"dari": simpang_eff + 1, "jarak": adjacency_matrix[simpang_eff][i]}}}
        if simpang_eff not in jejak:
            jejak+=[simpang_eff]
        simpang_eff = fid
        for j in range(jumlah_simpang):
            if dist[j]<dist[simpang_eff] and j not in jejak:
                simpang_eff = j
    if int(akhir) in alur or alur!={}:
        str_alur = akhir
        asal = int(akhir)
        while alur[asal]["dari"]!=int(awal):
            asal = alur[asal]["dari"]
            str_alur =  "%i -(%i)-> %s" %(asal, alur[asal]["jarak"] ,str_alur)
        str_alur =  "%i -(%i)-> %s" %(alur[asal]["dari"], alur[asal]["jarak"], str_alur)
        return dist[fid], str_alur
    else:
        return "not valid", "not valid"

print("Program ini akan memberikan output rute tercepat dari suatu peta.")
print("1. Simple\n2. ITB\n3. Buat sendiri")
choice = int(input("Pilih peta yang ingin digunakan(indexnya saja): "))

if choice==1:
    jumlah_simpang = 3
    adjacency_matrix = [
        [ 1, 3, 1],
        [ 2, 0, 1],
        [ 0, 1, 0]]
elif choice==2:
    jumlah_simpang = 23
    adjacency_matrix = [
        [0, 4, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
elif choice==3:
    jumlah_simpang, adjacency_matrix = matrix_baru()
else:
    print("pilihan tidak tersedia!")

if 0 < choice <= 3:
    c = "y"
    while c=="y" and (c!="n" or c!=""):
        start+=[input("Titik mulai/awal: ")]
        c = input("Masih ada lagi?(y/n): ")
    c = "y"
    while c=="y" and (c!="n" or c!=""):
        dest+=[input("Titik destinasi/tujuan: ")]
        c = input("Masih ada lagi?(y/n): ")
    for l in start:
        print("Rute tercepat dari titik %s" %l)
        print("Menuju       Jarak        Rute")
        for m in dest:
            jarak, rute = rute_eff(l, m)
            print(f"{m:>6}{jarak:>12}       ", rute)
