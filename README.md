# READ ME

---

### kasiski.py

**Paso 1.** Encontramos los patrones repetidos con sus posiciones.

![image.png](images/image.png)

**Paso 2.** Obtenemos las distancias entre cada una de las posiciones y las agregamos a una array. 

![image.png](images/image%201.png)

**Paso 3.** Sacamos los factores de cada distancia, y obtenemos los más comunes, en este caso los tres más comunes. 

![image.png](images/image%202.png)

**Paso 4.** Dividimos el texto cifrado en n grupos, siendo n el factor, y vamos agregando los caracteres del texto cifrado uno a uno en cada grupo, hasta que acabamos con todas las letras.  

![image.png](images/image%203.png)

**Paso 5.** Una vez, iteramos en cada grupo buscando las letras más comunes (las máximas letras igual de comunes), y con esto conseguimos nuestras posibles E’s. 

Después de eso, combinamos esas posibles letras para ver todas las combinaciones de posibles E’s. 

Después para cada combinación, conseguimos el posible shift o desplazamiento y con ello la key. 

Que utilizamos para intentar desencriptar cada texto. 

![image.png](images/image%204.png)

![image.png](images/image%205.png)

Una vez llegamos a las combinaciones con seis factores, cuando llegamos a `key = CFYPTO`, ya se empieza a vislumbrar texto entendible, comenzando con “**A**E**UCCES**E**FUL**”, que se puede entender como “A SUCCESSFUL”. Por lo tanto, la key está bien casi completamente, ya que el único error es en la segunda letra, entonces “**C**F**YPTO**”, aquí es donde se puede hacer la suposición de que la key real es:: “**CRYPTO**”.

![image.png](images/image%206.png)

En otro programa donde ya solo ingresamos la key y este nos lo desencripta, ingresé eso y me queda lo siguiente. 

### decryptKasiski.py

![image.png](images/image%207.png)

Por lo tanto la Key es **CRYPTO** y el texto: **A SUCCESSFUL CYBERSECURITY CULTURE CANNOT EXIST WITHOUT FIRST IDENTIFYING YOUR ORGANIZATION'S RISK TOLERANCE. THIS MEANS THERE NEEDS TO BE AN ESTABLISHED AGREEMENT ASSESSING WHAT DATA AND SYSTEMS MUST BE PROTECTED. THE LEVEL OF SECURITY NEEDED TO PROTECT THESE ASSETS AND HOW TO GO ABOUT SECURING THEM. THE ANSWERS TO THESE QUESTIONS ARE VITAL TO ANY AND ALL INFORMATION SECURITY POLICY FRAMEWORKS AND WILL DRIVE THE LEVEL OF SECURITY WITHIN THE ORGANIZATION FROM WHAT'S EXPECTED OF EACH EMPLOYEE TO THE OVERALL GOVERNANCE STRUCTURE.**

---

*References.*
