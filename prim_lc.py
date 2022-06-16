INF = 9999999  #definisi bilangan tertinggi
N = int(input("Masukkan jumlah vertex: ")) #input jumlah vertex

# Contoh dalam matriks ketetanggaan
# G = [[0, 19, 5, 0, 0],
#      [19, 0, 5, 9, 2],
#      [5, 5, 0, 1, 6],
#      [0, 9, 1, 0, 1],
#      [0, 2, 6, 1, 0]]

# Matriks Tetangga
# 0 280 0 0 0 0 0 0 0 0 0 0
# 280 0 140 1800 1100 800 0 0 0 0 0 0
# 0 140 0 1600 0 0 0 0 0 0 0 0
# 0 1800 1600 0 1700 0 0 0 0 0 0 0
# 0 1100 0 1700 0 650 2500 1500 0 0 0 0
# 0 800 0 0 650 0 2200 0 0 0 0 3300
# 0 0 0 0 2500 2200 0 0 150 0 0 0
# 0 0 0 0 1500 0 0 0 0 87 0 0
# 0 0 0 0 0 0 150 0 0 400 0 2800
# 0 0 0 0 0 0 0 870 400 0 1300 0
# 0 0 0 0 0 0 0 0 0 1300 0 3900
# 0 0 0 0 0 3300 0 0 2800 0 3900 0

G = []      # Untuk nampung matriks ketetanggaan

for _ in range(N):   # input matriks ketetanggaan
    x = [int(x) for x in input().split()]
    G.append(x)
print(*G,'\n',sep='\n')    # tampilkan matriks ketetanggan

seen = []        # buat array baru untuk vertex yg udah dikunjungi
for _ in range(N):
    seen.append(0)

seen[0] = True  # set vertex pertama udah dikunjungi
mst = 0 # buat variabel nampung mst

# printing for edge and weight
print("Edge : Weight\n")

for _ in range(N-1):
    minimum = INF   # set nilai min untuk dibandingkan sama bobot
    min_a = 0       # buat nampung indeks minimum
    min_b = 0
    for m in range(N):    # looping yang intinya kl dah dikunjungi, dicek yang
        if seen[m]:       # berhubungan, lalu cari yang paling kecil, di tiap vertex
            for n in range(N):
                if ((not seen[n]) and G[m][n]):  
                    # kl pasangannya belum dilihat, dan tentunya ada edge (kl dah terlihat berarti cycle)
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        min_a = m
                        min_b = n
    print(str(min_a) + " --> " + str(min_b) + " : " + str(G[min_a][min_b]))
    mst = mst + G[min_a][min_b] # jumlahkan ke mst
    seen[min_b] = True   # set udah dikunjungin

print(f'MST: {mst}') # cetak mst akhir
    
