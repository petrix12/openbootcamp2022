altura_cm = 183
altura_m = altura_cm / 100
peso_k = 102.3
altura_m_up = Math.ceil(altura_m)
altura_m_down = Math.floor(altura_m)
maximoValorJS = Number.MAX_VALUE;
boolMaxValor = maximoValorJS === (maximoValorJS + 1)

console.log("altura_cm: ", altura_cm)
console.log("altura_m: ", altura_m)
console.log("peso_k: ", peso_k)
console.log("altura_m_up: ", altura_m_up)
console.log("altura_m_down: ", altura_m_down)
console.log("maximoValorJS: ", maximoValorJS)
console.log("maximoValorJS + 1: ", maximoValorJS + 1)
console.log("boolMaxValor: ", boolMaxValor)