import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import argparse
import sys
import locale

def generate_citation(url, current_date):
    title = get_page_title(url)
    return f"{title} [en línia] [consulta: {current_date}] Disponible a: {url}"

def get_page_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No Title Found"
        return title
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return "Error accessing page"

def process_csv(input_csv_path, output_txt_path):

    df = pd.read_csv(input_csv_path, delimiter=';')
    
    output_lines = []
    
    for index, row in df.iterrows():
        url = row['url']
        query_datetime = row['datetime']
        output_line = generate_citation(url, query_datetime)
        output_lines.append(output_line)
    
    # Escriure la sortida al fitxer de text
    with open(output_txt_path, 'w') as f:
        for line in output_lines:
            f.write(line + '\n')

    print(f"Informació desada a {output_txt_path}")

def main():
    if len(sys.argv) == 1:
        print("No s'ha rebut cap paràmetre.")
        return
    
    locale.setlocale(locale.LC_TIME, 'ca_ES.UTF-8')

    parser = argparse.ArgumentParser(description="Genera una cita o multiples cites.")
    parser.add_argument('-u', '--url', type=str, help="Url per generar la cita")
    parser.add_argument('-f', '--fitxer', type=str, help="Nom del fitxer a processar")
    args = parser.parse_args()

    if args.url:
        current_date = date.today().strftime("%-d %B del %Y")
        print(generate_citation(args.url, current_date))
    else:
        input_csv_path = 'entrada.csv'  # Canvia això pel camí del teu arxiu d'entrada
        output_txt_path = 'sortida.txt'  # Fitxer on desarà la sortida
        process_csv(input_csv_path, output_txt_path)

if __name__ == "__main__":
    main()