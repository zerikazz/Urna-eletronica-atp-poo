import pickle
import csv
from typing import List, Hashable
from abc import ABCMeta, abstractmethod

class Pessoa:
    def __init__(self, nome: str, cpf: str, rg: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg

    def assinatura_eletronica(self) -> Hashable:
        return hash((self.__nome, self.__cpf, self.__rg))

    def __str__(self):
        return f'{self.__nome} (CPF: {self.__cpf}, RG: {self.__rg})'


class Candidato(Pessoa):
    def __init__(self, nome: str, cpf: str, rg: str, numero: int):
        super().__init__(nome, cpf, rg)
        self.__numero = numero

    def get_numero(self) -> int:
        return self.__numero

    def __str__(self):
        return f'Candidato {self.__numero} - {super().__str__()}'

class Vice(Pessoa):
    def __init__(self, nome: str, cpf: str, rg: str, numero: int):
        super().__init__(nome, cpf, rg)
        self.__numero = numero

    def get_numero(self) -> int:
        return self.__numero

    def __str__(self):
        return f'Vice {self.__numero} - {super().__str__()}'


class Eleitor(Pessoa):
    def __init__(self, nome: str, cpf: str, rg: str, titulo: int, secao: int, zona: int):
        super().__init__(nome, cpf, rg)
        self.__titulo = titulo
        self.secao = secao
        self.zona = zona

    def get_titulo(self) -> int:
        return self.__titulo

    def __str__(self):
        return f'Eleitor {self.__titulo} - {super().__str__()}'


class Transparencia(metaclass=ABCMeta):
    @abstractmethod
    def to_csv(self):
        pass

    @abstractmethod
    def to_txt(self):
        pass


class Urna(Transparencia):
    mesario: Pessoa
    __secao: int
    __zona: int
    __eleitores_presentes: List[Eleitor] = []
    __votos = {}

    def __init__(self, mesario: Pessoa, secao: int, zona: int,
                 candidatos: List[Candidato], eleitores: List[Eleitor]):
        self.mesario = mesario
        self.__secao = secao
        self.__zona = zona
        self.__nome_arquivo = f'{self.__zona}_{self.__secao}.pkl'
        self.__candidatos = candidatos
        self.__eleitores = [eleitor for eleitor in eleitores if eleitor.zona == zona and eleitor.secao == secao]

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_eleitor(self, titulo: int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return None

    def registrar_voto(self, eleitor: Eleitor, n_cand: int):
        self.__eleitores_presentes.append(eleitor)
        if n_cand in self.__votos:
            self.__votos[n_cand] += 1
        else:
            self.__votos['NULO'] += 1

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_secao(self):
        return self.__secao

    def get_zona(self):
        return self.__zona

    def get_titulo(self):
        return self.__eleitores_presentes

    def to_csv(self):
        with open(f'Transparencia_Urna_{self.__zona}_{self.__secao}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Seção', 'Zona', 'Título dos Eleitores Presentes'])

            for info in self.__eleitores_presentes:
                writer.writerow([self.__secao, self.__zona, info.get_titulo()])

    def to_txt(self):
        with open(f'Transparencia_Urna_{self.__zona}_{self.__secao}.txt', mode='w') as file:
            for info in self.__eleitores_presentes:
                file.write(str(info) + '\n')

    def __str__(self):
        info = f'Urna da seção {self.__secao}, zona {self.__zona}\n'
        info += f'Mesário: {self.mesario}\n'
        return info

if __name__ == "__main__":

    c1 = Candidato("Andressa Urach", "123123", "255255", 93)
    c2 = Candidato("Joana", "22222", "33333", 88)

    v1 = Vice("Marido da Lana del Rey", "123123", "255255", 93)
    c2 = Candidato("Joana", "22222", "33333", 88)

    e1 = Eleitor("Maria", "555666", "545454", 1, 42, 555)
    e2 = Eleitor("Carlos", "56888", "222222", 5, 56, 333)
    e3 = Eleitor("Eminem", "77777", "565499", 2, 54, 656)

    urna = Urna(e3, 54, 656, [c1, c2], [e1, e2, e3])

    urna.registrar_voto(e1, 99)

    urna.to_csv()
    urna.to_txt()

    print(urna)