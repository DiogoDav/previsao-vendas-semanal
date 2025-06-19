###### Para rodar com interface do usuário ######
##!pip install gradio

import gradio as gr

# função de previsão com os coeficientes ajustados
def calcular_modelo(D_Location, Promotion, D_MarketSize):
    D_MarketSize = {"Small": 1, "Medium": 2, "Large": 3}[D_MarketSize]
    resultado = (
        -35.7320441513142 +
        124.538140237919 * D_Location +
        -40.6416306569119 * (D_Location **2) +
        5.01548223566249 * (D_Location **3) +
        -0.210104769344876 * (D_Location **4) +
        -31.3152845561238 * Promotion +
        7.28454265511778 * (Promotion **2) +
        2.56058533989902 * (D_MarketSize **2)
    )
    # return f"$ {round(resultado, 2)} MIL"
    return  "$ " + str( round( resultado, 2 )  ) + " MIL"

# Interface do Gradio
interface = gr.Interface(
    fn=calcular_modelo,
    inputs=[
        gr.Number(label="Codigo Location 1 a 10", minimum=1, maximum=10),
        gr.Number(label="Promotion 1 a 3", minimum=1, maximum=3),
        gr.Dropdown(label="MarketSize", choices=["Small", "Medium", "Large"])  ],
    
    outputs=gr.Textbox(label="Previsão de Vendas na semana"),
    title="Modelo de Regressão Polinomial Múltipla",
    description="Previsão de vendas semanais com base em localização, promoção e tamanho do mercado."
)

# Executar interface
interface.launch(server_name="0.0.0.0", server_port=8080)
