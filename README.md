# CP 

Este projeto usa o ESP32 para coletar dados de um potenciômetro, calcular as características (média, desvio padrão, RMS, PTP) e classificar com um modelo de Decision Tree.


## Como Rodar

### 1.  Preparar o Hardware

Conectar o potenciômetro ao pino 34 do ESP32 (pino analógico).

Conectar os LEDs para mostrar a classificação:
- LED_XOR_TRUE: acende quando a classificação for 1.

- LED_XOR_FALSE: acende quando a classificação for 0.

### 2. Carregar o Código no ESP32

Abrir o código no Arduino IDE.

Selecionar a placa ESP32 e carregar o código

### 3. Testando a Classificação

O modelo classifica os dados e acende o LED correspondente.

