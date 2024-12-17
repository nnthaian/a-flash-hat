import pygame

BLACK = (0,0,0)
pygame.font.init()

class Button:
    '''
    this class is to create a form for all buttons using this class and check if the user has clicked it or not.
    :param: image: the image we want the button to look like
    :param: x_pos: the x-position of the button
    :param: y_pos: the y-position of the button
    :param: screen: the surface screen in the main.py
    '''
    def __init__(self, x_pos, y_pos, image):
        self.image = (image).convert_alpha()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        self.clicked = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def check_click_only(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

    def show(self, screen):
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update_n_check_click(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

# code to wrap text from https://github.com/ColdrickSotK/yamlui/blob/master/yamlui/util.py#L82-L143

def wrap_text(text, font, width):
    """Wrap text to fit inside a given width when rendered.
    :param text: The text to be wrapped.
    :param font: The font the text will be rendered in.
    :param width: The width to wrap to.
    """
    text_lines = text.replace('\t', '    ').split('\n')
    if width is None or width == 0:
        return text_lines

    wrapped_lines = []
    for line in text_lines:
        line = line.rstrip() + ' '
        if line == ' ':
            wrapped_lines.append(line)
            continue

        # Get the leftmost space ignoring leading whitespace
        start = len(line) - len(line.lstrip())
        start = line.index(' ', start)
        while start + 1 < len(line):
            # Get the next potential splitting point
            next = line.index(' ', start + 1)
            if font.size(line[:next])[0] <= width:
                start = next
            else:
                wrapped_lines.append(line[:start])
                line = line[start+1:]
                start = line.index(' ')
        line = line[:-1]
        if line:
            wrapped_lines.append(line)
    return wrapped_lines


def render_text_list(lines, font, colour = BLACK):
    """
    Draw multiline text to a single surface with a transparent background.
    Draw multiple lines of text in the given font onto a single surface
    with no background colour, and return the result.
    :param lines: The lines of text to render.
    :param font: The font to render in.
    :param colour: The colour to render the font in, default is black.
    """
    rendered = [font.render(line, True, colour).convert_alpha()
                for line in lines]

    line_height = font.get_linesize()
    width = max(line.get_width() for line in rendered)
    tops = [int(round(i * line_height)) for i in range(len(rendered))]
    height = tops[-1] + font.get_height()

    surface = pygame.Surface((width, height)).convert_alpha()
    surface.fill((0, 0, 0, 0))
    for y, line in zip(tops, rendered):
        surface.blit(line, (0, y))

    return surface

class Card():
    WORD_FONT = pygame.font.Font('other/Marykate-Regular.ttf', 50)
    DEFINITION_FONT = pygame.font.Font('other/Marykate-Regular.ttf', 40)
    CARD_WIDTH = 325
    def __init__(self, word, definition):

        self.word = Card.WORD_FONT.render(word, True, BLACK)
        self.definition = render_text_list(wrap_text(definition, Card.DEFINITION_FONT, Card.CARD_WIDTH), Card.DEFINITION_FONT, BLACK)
        self.wordRect = self.word.get_rect()
        self.defRect = self.definition.get_rect()

    def drawCard(self, word_pos, def_pos, screen):
        self.wordRect.center = word_pos
        self.defRect.center = def_pos
        screen.blit(self.word, self.wordRect)
        screen.blit(self.definition, self.defRect)

class Page():
    lstCoor3Words = [(250,110),(750,110),(500,425)]
    lstCoor3Defs = [(250,220),(750,220),(500,550)]

    MAX_PER_PAGE = 3
    def __init__(self, page_number, page_content):
        self.page_number = page_number
        self.page_content = page_content #which is a list of 3 cards
        self.active = False
        self.lstCards = []

    def draw(self, screen): #coor stands for coordinates
        for (card, coorWord, coorDef) in zip(self.page_content, Page.lstCoor3Words, Page.lstCoor3Defs):
            self.lstCards.append(card)
            card.drawCard(coorWord, coorDef, screen)

    def numeratePage(self, totalPage, screen):
        PAGE_NUMBER_COLOR = (40,178,141)
        PAGE_NUMBER_FONT = pygame.font.Font('other/Marykate-Regular.ttf', 25)
        page_number = str(str((self.page_number+1))+"/"+str(totalPage))
        page_number_rendered = PAGE_NUMBER_FONT.render(page_number, True, PAGE_NUMBER_COLOR)
        page_number_rect = page_number_rendered.get_rect()
        page_number_rect.center = (800, 600)
        screen.blit(page_number_rendered, page_number_rect)

    @classmethod
    def createCardsEachPage(cls, lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
