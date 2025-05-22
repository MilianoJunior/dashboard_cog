from flask import Flask, Response, render_template, url_for
from components.graficos import Grafico
import time
import random
import json

app = Flask(__name__, static_folder='static')

# Função para simular dados dinâmicos
def obter_dados_atualizados():
    # Simula dados de temperatura para 6 sensores
    sensores = []
    for i in range(6):
        # Temperatura base de 69°C com variação aleatória
        temp_base = 69.0
        variacao = random.uniform(-2.0, 2.0)
        temperatura = temp_base + variacao
        
        # Calcula o status baseado no desvio
        desvio = abs(temperatura - temp_base)
        if desvio > 8.0:
            status = "CRÍTICO"
        elif desvio > 4.0:
            status = "ALERTA"
        else:
            status = "NORMAL"
            
        sensores.append({
            "id": f"card-{i}",
            "title": f"Sensor Mancal G{i + 1}",
            "setpoint": temp_base,
            "actualTemp": temperatura,
            "status": status.lower(),
            "statusText": status,
            "deviation": temperatura - temp_base
        })
    return sensores

@app.route('/')
def index():
    return render_template('temperaturas.html')

@app.route('/atualizar_grafico')
def atualizar_grafico():
    def gerar_eventos():
        while True:
            try:
                dados = obter_dados_atualizados()
                # Converte os dados para JSON
                dados_json = json.dumps(dados)
                yield f"data: {dados_json}\n\n"
                time.sleep(2.5)  # Atualiza a cada 2.5 segundos
            except Exception as e:
                print(f"Erro ao gerar dados: {e}")
                yield f"data: {{'error': 'Erro ao atualizar dados'}}\n\n"
                time.sleep(5)
    return Response(gerar_eventos(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)

'''
Relato para boletim de ocorrência

Relato, não como testemunha ocular que por volta das 02:30 da manhã, o vigilante Neri Caetano de Oliveira que estava na guarita 07, localizado no semi-aberto da Penitenciária Agricula de Chapecó, escutou um barulho, sendo assim, vizualizou 1(um) homem, que quando avistado, correu para o mato, na area de influencia da penitenciária, nesse momento, ouvisse dois disparos de arma de fogo não direcional. Houve comunicação pelo rádio sobre o ocorrido, os policiais foram acionados para o local, onde foi encontrado dois molotes com 19 celulares e 21 carregadores de celulares. Além disso, foi verificado na cela 04 do semi-aberto que as grades e cerca estavam cortadas, que seria a provavel entrada do malote. Em realização de chamanda nominal, foi verificado que não houve fugas.



Informo, não como testemunha ocular, que por volta das 2h30 da madrugada, o vigilante Neri Caetano de Oliveira, que estava na guarita 07, localizada no regime semiaberto da Penitenciária Agrícola de Chapecó, ouviu um barulho. Ao averiguar, visualizou um homem que, ao ser avistado, correu em direção ao mato, na área de influência da penitenciária. Nesse momento, foram ouvidos dois disparos de arma de fogo sem direção definida, possivelmente dos invasores, conforme relato do vigilante Neri Caetano de Oliveira.

O ocorrido foi comunicado via rádio, e os policiais foram acionados para o local. Durante a varredura, foram encontrados dois malotes contendo 19 celulares e 21 carregadores de celular. Além disso, foi verificado que, na cela 04 do regime semiaberto, as grades e a cerca estavam cortadas, indicando a provável entrada dos malotes.

Após a realização de chamada nominal, constatou-se que não houve fugas.



'''