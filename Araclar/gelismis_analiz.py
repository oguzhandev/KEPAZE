#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.linear_model import LinearRegression
import networkx as nx
import matplotlib.pyplot as plt



def web_scrape():
    url = input("Analiz edilecek URL: ")
    selector = input("Veri almak istediğiniz CSS seçici (boş bırakılabilir): ")
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        # İlk deneme
        elements = soup.select(selector) if selector else soup.find_all("p")
        if not elements:
            print("Belirtilen alan bulunamadı. Tag veya class adı girin:")
            selector = input("CSS seçici: ")
            elements = soup.select(selector)

        if not elements:
            print("Veri çekilemedi.")
            return

        texts = [el.get_text(separator=" ", strip=True) for el in elements]
        full_text = "\n".join(texts)
        print("\nÇekilen Veriler:\n")
        print(full_text)

        save = input("Veriyi 'scrape_output.txt' olarak kaydetmek ister misiniz? (E/H): ").lower()
        if save == "e":
            with open("scrape_output.txt", "w", encoding="utf-8") as f:
                f.write(full_text)
            print("Veriler kaydedildi.")
    except Exception as e:
        print("Hata:", e)


def regression_analysis():
    path = input("CSV dosya yolu (x,y kolonları): ")
    try:
        df = pd.read_csv(path)
        model = LinearRegression()
        X = df[['x']]
        y = df['y']
        model.fit(X, y)
        print("Regresyon katsayısı:", model.coef_[0])
        print("Regresyon sabiti:", model.intercept_)
    except Exception as e:
        print("Hata:", e)


def relation_graph():
    print("Kenarları 'kaynak hedef' formatında girin. Boş satır bitirir.")
    edges = []
    while True:
        line = input()
        if not line:
            break
        parts = line.split()
        if len(parts) != 2:
            print("Geçersiz format")
            continue
        edges.append((parts[0], parts[1]))
    if not edges:
        print("Kenar girilmedi")
        return
    G = nx.Graph()
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True)
    plt.savefig("gelismis_analiz_graph.png")
    plt.close()
    print("Diagram 'gelismis_analiz_graph.png' olarak kaydedildi.")


def correlation_analysis():
    path = input("Korelasyon için CSV dosya yolu: ")
    try:
        df = pd.read_csv(path)
        corr = df.corr(numeric_only=True)
        print("Korelasyon Matrisi:\n", corr)
        plt.imshow(corr, cmap='coolwarm', interpolation='none')
        plt.colorbar()
        plt.xticks(range(len(corr)), corr.columns, rotation=90)
        plt.yticks(range(len(corr)), corr.columns)
        plt.tight_layout()
        plt.savefig("gelismis_korelasyon.png")
        plt.close()
        print("Heatmap 'gelismis_korelasyon.png' olarak kaydedildi.")
    except Exception as e:
        print("Hata:", e)


def network_metrics():
    print("Kenarları 'kaynak hedef' formatında girin. Boş satır bitirir.")
    edges = []
    while True:
        line = input()
        if not line:
            break
        parts = line.split()
        if len(parts) != 2:
            print("Geçersiz format")
            continue
        edges.append((parts[0], parts[1]))
    if not edges:
        print("Kenar girilmedi")
        return
    G = nx.Graph()
    G.add_edges_from(edges)
    deg = nx.degree_centrality(G)
    bet = nx.betweenness_centrality(G)
    clo = nx.closeness_centrality(G)
    print("\nMerkezilik Metrikleri:")
    for node in G.nodes():
        print(f"{node} -> Degree:{deg[node]:.2f} Betweenness:{bet[node]:.2f} Closeness:{clo[node]:.2f}")
    nx.draw(G, with_labels=True)
    plt.savefig("gelismis_ag.png")
    plt.close()
    print("Ağ grafiği 'gelismis_ag.png' olarak kaydedildi.")


def data_summary():
    path = input("CSV dosya yolu: ")
    try:
        df = pd.read_csv(path)
        print(df.describe(include='all'))
    except Exception as e:
        print("Hata:", e)


def main():
    print("\nGELİŞMİŞ ANALİZ ARACI")
    while True:
        print("\n1) Web Kazıma")
        print("2) Regresyon Analizi")
        print("3) İlişki Diyagramı Oluştur")
        print("4) Korelasyon Analizi")
        print("5) Ağ Metrikleri")
        print("6) Veri Özeti")
        print("7) Çıkış")
        secim = input("Seçiminiz: ")
        if secim == '1':
            web_scrape()
        elif secim == '2':
            regression_analysis()
        elif secim == '3':
            relation_graph()
        elif secim == '4':
            correlation_analysis()
        elif secim == '5':
            network_metrics()
        elif secim == '6':
            data_summary()
        elif secim == '7':
            break
        else:
            print("Geçersiz seçim")


if __name__ == "__main__":
    main()
