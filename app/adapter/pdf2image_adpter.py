import pdf2image
import os
import sys


class PDFConverter:
    def __init__(self, poppler_path=None, dev_mode=False):
        """
        Inicializa o PDFConverter com o caminho para os binários do Poppler.

        Se nenhum caminho for fornecido, o construtor tentará usar o PATH do sistema.

        Parâmetros:
        - poppler_path (str, opcional): Caminho para os binários do Poppler. Se None, usará o PATH do sistema.
        - dev_mode (bool, opcional): Se True, define um caminho padrão para os binários do Poppler (usado para desenvolvimento).
        """
        if dev_mode:
            poppler_path = r"C:\poppler\Library\bin"

        self.poppler_path = poppler_path or self.get_poppler_cmd()

    def get_poppler_cmd(self):
        """
        Retorna o caminho para os binários do Poppler, seja em um
        pacote do PyInstaller ou em um ambiente regular.

        Retorna:
        - str ou None: Caminho para os binários do Poppler, ou None se não encontrado.
        """
        if hasattr(sys, "_MEIPASS"):
            # Ao executar a partir do pacote PyInstaller,
            # usa os binários do Poppler incluídos.
            return os.path.join(sys._MEIPASS, "poppler/bin")
        else:
            # Se não estiver em um pacote do PyInstaller, assume que o Poppler está no PATH.
            return None

    def convert_pdf_to_images(self, pdf_path):
        """
        Converte o PDF fornecido em imagens e retorna uma lista de objetos
        da classe PIL Image.

        Parâmetros:
        - pdf_path (str): Caminho para o arquivo PDF a ser convertido.

        Retorna:
        - list: Lista de objetos de imagem (PIL) correspondentes às páginas do PDF.
        """
        return pdf2image.convert_from_path(
            pdf_path, poppler_path=self.poppler_path
        )
