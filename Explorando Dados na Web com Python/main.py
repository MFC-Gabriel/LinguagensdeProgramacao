"""
main.py
Script principal — executa os três níveis da atividade.
"""

import nivel1_basico
import nivel2_intermediario
import nivel3_avancado


def main():
    print("\n🚀 Iniciando atividade: Explorando Dados na Web com Python\n")

    print("\n########## NÍVEL 1 — BÁSICO ##########")
    nivel1_basico.executar()

    print("\n########## NÍVEL 2 — INTERMEDIÁRIO ##########")
    nivel2_intermediario.executar()

    print("\n########## NÍVEL 3 — AVANÇADO ##########")
    nivel3_avancado.executar()

    print("\n🎉 Atividade concluída! Verifique os arquivos gerados:")
    print("   - imagem_aleatoria.jpg")
    print("   - livros.csv")
    print("   - paises_populacao.csv")


if __name__ == "__main__":
    main()