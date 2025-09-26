Algoritmo f
	Definir peso,estatura,IMC Como Real;
	Escribir"peso"
	leer peso;
	Escribir "estatura"
	Leer estatura
	IMC <-peso/(estatura)^2
	Escribir "El IMC es:",IMC
	si IMC <=0 Entonces
		Escribir "anda mal"
	Sino 
		Escribir "anda bien"
	FinSi
FinAlgoritmo
