import pygame
import sys
import os

SCREENWIDTH, SCREENHEIGHT = 900, 935
FPS = 60

# --- FUNÇÃO AUXILIAR PARA CORRIGIR CAMINHOS ---
# Usa o diretório do script como base para carregar assets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def get_asset_path(relative_path):
    # O arquivo screens.py está dentro de RunningFox/. 
    # Então, ele constrói o caminho a partir de onde o screens.py está.
    # Ex: BASE_DIR + 'imagens_pygame/imagem_start.png'
    return os.path.join(BASE_DIR, relative_path)

# --- CLASSE BASE ---
class BaseScreen:
    def __init__(self, display, gsm, bg_path):
        self.display = display
        self.gsm = gsm
        
        # Usa a função auxiliar para garantir que o caminho do arquivo está correto
        full_bg_path = get_asset_path(bg_path) 
        
        # Carrega a imagem de fundo
        self.bg = pygame.image.load(full_bg_path).convert()
        self.bg = pygame.transform.scale(self.bg, (SCREENWIDTH, SCREENHEIGHT))
        self.font_title = pygame.font.SysFont(None, 72)
        self.font_text = pygame.font.SysFont(None, 36)

    def draw_centered(self, text, font, y):
        surface = font.render(text, True, (255, 255, 255))
        rect = surface.get_rect(center=(SCREENWIDTH // 2, y))
        self.display.blit(surface, rect)
        return rect # Retorna o Rect, essencial para o botão


# --- TELA DE INÍCIO ---
class Start(BaseScreen):
    def __init__(self, display, gsm):
        # Apenas o caminho RELATIVO ao screens.py
        super().__init__(display, gsm, "imagens_pygame/imagem_start.png") 
        self.start_button_rect = None 
        button_image_path = get_asset_path("imagens_pygame/botao_start.png")
        
        # MUDANÇA AQUI: Usando .convert() em vez de .convert_alpha() para JPEG
        self.start_button_image = pygame.image.load(button_image_path).convert_alpha()
        target_width = 400
        # --- ADICIONE ESTAS DUAS LINHAS PARA REDIMENSIONAR ---
        new_width = 300  # Exemplo: Defina a largura desejada
        new_height = 100 # Exemplo: Defina a altura desejada

        original_width, original_height = self.start_button_image.get_size()
        
        # 2. Calcula a nova altura para manter a proporção (aspect ratio):
        new_height = int(original_height * (target_width / original_width))

        self.start_button_image = pygame.transform.scale(self.start_button_image, (target_width, new_height))
        # ----------------------------------------------------

        # Cria a imagem para o estado de HOVER (Efeito mais escuro)
        self.start_button_hover_image = self.start_button_image.copy()
        self.start_button_hover_image.fill((50, 50, 50, 0), special_flags=pygame.BLEND_RGB_SUB)

    def handle_event(self, event):
        # Lógica do clique do mouse (Botão Esquerdo)    
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.start_button_rect and self.start_button_rect.collidepoint(event.pos):
                self.gsm.set_state('level')
        
        # Alternativa de tecla (Opcional, mas útil)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
             self.gsm.set_state('level')

    def run(self):
        self.display.blit(self.bg, (0, 0))
       
        
        button_y_pos = SCREENHEIGHT // 2 # Move o botão um pouco para baixo da primeira linha de texto

        mouse_pos = pygame.mouse.get_pos()
        current_button_image = self.start_button_image
        
        # Centraliza a imagem e define o Rect (O Rect é o que detecta o clique)
        self.start_button_rect = current_button_image.get_rect(center=(SCREENWIDTH // 2, button_y_pos))

        # 2. Verifica o hover e desenha o destaque
        if self.start_button_rect.collidepoint(mouse_pos):
           current_button_image = self.start_button_hover_image
        
        # Desenha a imagem do botão (ou a imagem de hover)
        self.display.blit(current_button_image, self.start_button_rect)
        # O Rect é atualizado em toda iteração do loop, garantindo que a detecção de clique funcione.

# --- TELA DO JOGO ---
class Level(BaseScreen):
    def __init__(self, display, gsm):
        super().__init__(display, gsm, "imagens_pygame/level_1.png")

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            self.gsm.set_state('end')

    def run(self):
        self.display.blit(self.bg, (0, 0))
        self.draw_centered("LEVEL - Pressione [E] para encerrar", self.font_text, SCREENHEIGHT - 100)


# --- TELA FINAL ---
class End(BaseScreen):
    def __init__(self, display, gsm):
        super().__init__(display, gsm, "imagens_pygame/game_over.png")

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.gsm.set_state('start')
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    def run(self):
        self.display.blit(self.bg, (0, 0))
        self.draw_centered("FIM DE JOGO", self.font_title, SCREENHEIGHT // 3)
        self.draw_centered("Pressione [R] para reiniciar ou [Q] para sair", self.font_text, SCREENHEIGHT // 2)


# --- GERENCIADOR DE ESTADOS ---
class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state


# --- EXECUÇÃO PRINCIPAL ---
class Game:
    # ... (métodos Game.__init__ e Game.run)
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption("Running Fox Game")
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)
        self.end = End(self.screen, self.gameStateManager)

        self.states = {'start': self.start, 'level': self.level, 'end': self.end}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.states[self.gameStateManager.get_state()].handle_event(event)

            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            self.clock.tick(FPS)
    

if __name__ == '__main__':
    game = Game()
    game.run()