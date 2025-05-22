class Grafico:
    def __init__(self, dados, titulo="Gráfico"):
        self.dados = dados
        self.titulo = titulo
        self.cores = ["#4CAF50", "#2196F3", "#FFC107", "#9C27B0", "#F44336"]

    def gerar_html(self):
        if not self.dados:
            return '<div class="alert alert-warning">Sem dados para exibir</div>'
            
        categorias = [d[0] for d in self.dados]
        valores = [d[1] for d in self.dados]
        max_valor = max(valores) if valores else 1
        
        html = []
        html.append('<div class="grafico-container">')
        html.append(f'<h2 class="text-center mb-4">{self.titulo}</h2>')
        html.append('<div class="grafico-barras">')
        
        for i, (cat, val) in enumerate(zip(categorias, valores)):
            porcentagem = int((val / max_valor) * 100)
            cor = self.cores[i % len(self.cores)]
            
            html.append(f'''
                <div class="barra-container">
                    <div class="barra-label">{cat}</div>
                    <div class="barra-wrapper">
                        <div class="barra" style="width: {porcentagem}%; background-color: {cor};">
                            {val}
                        </div>
                    </div>
                </div>
            ''')
        
        html.append('</div>')
        html.append('</div>')
        
        return ''.join(html)

    def gerar_css(self):
        return '''
        .grafico-container {
            max-width: 800px;
            margin: 20px auto;
            padding: 15px;
        }
        .grafico-barras {
            margin-top: 15px;
        }
        .barra-container {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
            padding: 5px 0;
        }
        .barra-label {
            min-width: 100px;
            text-align: right;
            padding-right: 15px;
            font-weight: bold;
        }
        .barra-wrapper {
            flex: 1;
            background: #eee;
            border-radius: 4px;
            overflow: hidden;
        }
        .barra {
            min-height: 25px;
            line-height: 25px;
            text-align: left;
            padding: 0 10px;
            color: white;
            font-weight: bold;
            transition: width 0.3s ease;
        }
        .barra-texto {
            display: inline-block;
            vertical-align: middle;
        }
        '''