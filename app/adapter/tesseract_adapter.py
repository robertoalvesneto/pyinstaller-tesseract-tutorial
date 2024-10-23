import pytesseract
import os
import sys
import platform


class TesseractOCR:
    def __init__(
        self, lang="por", tesseract_cmd=None, tessdata_dir=None, dev_mode=False
    ):
        """
        Inicializa o TesseractOCR com a configuração desejada.

        Parâmetros:
        - lang (str): O código do idioma para o OCR. O padrão é "por" (português).
        - tesseract_cmd (str, opcional): Caminho para o executável do Tesseract. Se None, tentará detectar automaticamente.
        - tessdata_dir (str, opcional): Diretório onde os dados de idioma do Tesseract estão localizados.
        - dev_mode (bool, opcional): Se True, define caminhos padrão para o executável e dados do Tesseract (usado para desenvolvimento).
        """
        if dev_mode:
            tesseract_cmd = r"C:\vcpkg\installed\x64-windows-static\tools\tesseract\tesseract.exe"
            tessdata_dir = (
                r"C:\vcpkg\installed\x64-windows-static\share\tessdata"
            )

        self.lang = lang

        # Se o caminho do Tesseract for fornecido, configura o comando
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        else:
            # Detecta a plataforma e ajusta o caminho do Tesseract conforme necessário
            pytesseract.pytesseract.tesseract_cmd = self.get_tesseract_cmd()

        # Configura o TESSDATA_PREFIX se fornecido ou necessário
        if tessdata_dir:
            os.environ["TESSDATA_PREFIX"] = tessdata_dir
        else:
            self.set_tessdata_prefix()

    def get_tesseract_cmd(self):
        """
        Retorna o caminho do executável do Tesseract, dependendo da plataforma.

        No Windows, tenta usar o caminho apropriado (incluindo em bundles do PyInstaller).
        No Linux, assume-se que o Tesseract está no PATH.

        Retorna:
        - str: Caminho para o executável do Tesseract.
        """
        if platform.system() == "Windows":
            if hasattr(sys, "_MEIPASS"):
                # Quando executando a partir de um bundle do PyInstaller no Windows
                return os.path.join(sys._MEIPASS, "tesseract.exe")
            else:
                # Assume que o Tesseract está disponível no PATH ou o caminho foi passado
                return "tesseract"
        else:
            # No Linux, assume que o Tesseract está instalado globalmente
            return "tesseract"

    def set_tessdata_prefix(self):
        """
        Configura a variável de ambiente TESSDATA_PREFIX para garantir que o Tesseract encontre
        corretamente os arquivos de dados de idiomas.

        No Windows, ajusta o caminho com base na localização do executável.
        No Linux, não faz nada a menos que explicitamente configurado.
        """
        if platform.system() == "Windows":
            if hasattr(sys, "_MEIPASS"):
                # Quando executando a partir de um bundle do PyInstaller no Windows
                os.environ["TESSDATA_PREFIX"] = os.path.join(
                    sys._MEIPASS, "tessdata"
                )
            else:
                # Usa o diretório onde o tesseract.exe está localizado
                tesseract_dir = os.path.dirname(
                    pytesseract.pytesseract.tesseract_cmd
                )
                os.environ["TESSDATA_PREFIX"] = os.path.join(
                    tesseract_dir, "tessdata"
                )

    def image_to_string(self, image, config=None):
        """
        Converte uma imagem em texto utilizando Tesseract OCR.

        Parâmetros:
        - image: A imagem a ser convertida em texto.
        - config (str, opcional): Configurações adicionais para o Tesseract.

        Retorna:
        - str: O texto extraído da imagem.
        """
        return pytesseract.image_to_string(
            image, lang=self.lang, config=config
        )
