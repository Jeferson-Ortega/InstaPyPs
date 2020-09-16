# -*- coding: utf-8 -*-

import win32com.client as windows
import os
import sys

class geradorDePostsInstagram:

    def __init__(self):
        print("Abrindo Photoshop....")
        self.App = windows.Dispatch("Photoshop.Application")
        self.baseDir = str(os.getcwd())

        self.__setTemplate()
        self.__processarPastaDeImagens()

    def __setTemplate(self):
        template = os.listdir('template')

        self.template = os.path.join(self.baseDir, "template", template[0])
        
    def __processarPastaDeImagens(self):

        images = os.listdir(os.path.join('content', 'images'))
        texts = os.listdir(os.path.join('content', 'texts'))

        for image in images:
            image_path = os.path.join(self.baseDir, "content", "images", image)
            text_name = os.path.splitext(image)[0]+".txt"
            textoPost = ""

            if(text_name in texts):
                with open(os.path.join(self.baseDir, "content","texts", text_name), encoding='utf-8') as textoPost:
                    textoPost = textoPost.readlines()[0]


            self.__manipularImagemDeFundo(self.App, image_path)
            self.__manipularTemplate(self.App, self.template, textoPost)
            self.__salvarArquivo(self.App, image)
        
        self.__finalizarProcesso()

    def __manipularImagemDeFundo(self, App, local):
        App.Open(local)
        App.DisplayDialogs = 3
        print("============================================")
        print(f"Abrindo imagem de Fundo em {local}")

        document = App.Application.ActiveDocument

        imagemDeFundo = document.ArtLayers.Item(1)
        imagemDeFundo.Copy()

        document.Close(2)

    def __manipularTemplate(self, App, local, textoPost=""):
        App.Open(local)
        print(f"Abrindo template em {local}")
        App.DisplayDialogs = 3

        doc = App.Application.ActiveDocument

        titulo_post = doc.ArtLayers["post-title"]
        texto_da_layer = titulo_post.TextItem
        texto_da_layer.contents = textoPost
        imagem = doc.ArtLayers["post-image"]
        nova_layer = doc.Paste()
        nova_layer.Move(imagem, 3)
        nova_layer.Resize(150, 150, 5)
        nova_layer.Translate(-3, 0)
    
    def __salvarArquivo(self, App, name):
        doc = App.Application.ActiveDocument
        path_to_save = os.path.join(self.baseDir, "generated", "posts", name)

        options = windows.Dispatch('Photoshop.ExportOptionsSaveForWeb')
        options.Format = 13
        options.png8 = False

        doc.Export(ExportIn=path_to_save, ExportAs=2, Options=options)
        print(f"Arquivo salvo em {path_to_save}")
        print("============================================")
        
        doc.Close(2)
    
    def __finalizarProcesso(self):
        print("Fechando Photoshop....")
        self.App.Quit()
        print("Processo Finalizado")

posts = geradorDePostsInstagram()