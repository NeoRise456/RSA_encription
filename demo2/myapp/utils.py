import random

class Reader:
    lines = list()
    data = list()
    
    def __init__(self) -> None:
        pass
    
    

class ProcesadorDeTexto:
    def __init__(self, texto):
        self.texto = texto

    def procesar(self):
        # Aquí puedes realizar el procesamiento que necesites con el texto
        return self.texto.upper()  # Ejemplo: convierte el texto a mayúsculas

class Linear_math:
    def __init__(self) -> None:
        pass
    def mcd(self,a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def linear_congruence(self,a, b, m):
        if b == 0:
            return 0
        if a < 0:
            a = -a
            b = -b
        b %= m
        while a > m:
            a -= m
        return (m * self.linear_congruence(m, -b, a) + b) // a

class Criptography:
    p = 31
    q = 47
    n = p * q
    e = 0
    d = 0
    
    euler_function = (p - 1) * (q - 1)
    operations = Linear_math()
    
    
    
    def __init__(self) -> None:
        pass
    
    def set_p(self,x:int) -> None:
        self.p = x

    def set_q(self,x:int) -> None:
        self.q = x
    
    
    
    def get_euler(self) -> int:
        return (self.p - 1) * (self.q - 1)
    
    def find_d(self) -> None:
        d = 2
        nums = list()
        for d in range(2,self.euler_function):
            num = self.operations.mcd(d,self.euler_function)
            if num == 1:
                nums.append(d)
        #index_num = random.randint(0,len(nums))
        self.d = nums[5]
    
    def get_keys(self) -> None:
        self.find_d()

        #dE === 1 mod phi
        #aX ≡ b (mod m)
        self.e = self.operations.linear_congruence(self.d,1,self.euler_function)

    def process_text(self,text:str) -> list:
        lines = list(text.splitlines(keepends=True))
        lines = [list(e) for e in lines]
        data = [[ord(char) for char in line] for line in lines]
        return data 
    
    def decript(self,text:str) -> str:
        data = self.process_text(text)
            #monse = self.process_text('monse')
        
        desencripted_data = [[chr((pow(line,self.d))%self.n) for line in lines] 
                            for lines in data] #list comprenhension
        
        lineas = [''.join(linea) for linea in desencripted_data]
        texto_reconstruido = ''.join(lineas)
        
        return texto_reconstruido
    
    def encript(self,text:str) -> str:
        data = self.process_text(text)
        encripted_data = [[chr((pow(line,self.e)) % self.n) for line in lines] for lines in data]
        
        lineas = [''.join(linea) for linea in encripted_data]
        texto_reconstruido = ''.join(lineas)
        return texto_reconstruido