#!/usr/bin/env python
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def load_edges():
    path = input("Kaynak-hedef kolonlu CSV dosya yolu: ")
    try:
        df = pd.read_csv(path)
        return list(zip(df[df.columns[0]], df[df.columns[1]]))
    except Exception as e:
        print("Hata:", e)
        return []


def analyze(edges):
    if not edges:
        print("Veri bulunamadı")
        return
    G = nx.Graph()
    G.add_edges_from(edges)
    print("Düğüm sayısı:", G.number_of_nodes())
    print("Kenar sayısı:", G.number_of_edges())

    deg = nx.degree_centrality(G)
    bet = nx.betweenness_centrality(G)
    clo = nx.closeness_centrality(G)
    print("\nMerkezilik Metrikleri:")
    for node in G.nodes():
        print(f"{node}: Degree {deg[node]:.2f} Bet {bet[node]:.2f} Clo {clo[node]:.2f}")

    save = input("Grafiği kaydetmek ister misiniz? (E/H): ").lower()
    if save == 'e':
        nx.draw(G, with_labels=True)
        plt.savefig("sosyal_ag.png")
        plt.close()
        print("Grafik 'sosyal_ag.png' olarak kaydedildi.")


def main():
    print("\nSOSYAL AĞ ANALİZİ ARACI")
    edges = load_edges()
    analyze(edges)


if __name__ == "__main__":
    main()
