"""
Arcade - maison

TP5 - Alexander Precup, 402
Construire une image d'une maison avec la librairie Arcade
"""

import arcade

# Dimensions écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Arcade - maison"


def dessiner_arriere_plan():
    """
    Dessiner l'arrière-plan : le ciel et le gazon.
    """

    # Ciel - rectangle bleu-ciel
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT/3, arcade.color.SKY_BLUE)
    # Gazon - rectangle vert foncé
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT/3, 0, arcade.color.DARK_GREEN)


def dessiner_rectangle(x, y, largeur, longueur, couleur):
    """
    Dessiner un rectangle.

    Paramètres:

    - x: le centre du rectangle sur l'axe des X.
    - y: le centre du rectangle sur l'axe des Y.
    - longueur: longueur du rectangle.
    - largeur: longueur du rectangle.
    - couleur: couleur du rectangle.
    """

    arcade.draw_lrtb_rectangle_filled(x, x + largeur, y + longueur, y, couleur)


def dessiner_fenetres():
    """
    Dessiner deux fenêtres avec des rectangles et des lignes.

    """

    # Fenêtre 1 - un rectangle et deux lignes
    dessiner_rectangle(325, 325, 30, 30, arcade.csscolor.WHITE)
    arcade.draw_line(324, 337.5, 355, 337.5, arcade.csscolor.BLACK, 1)
    arcade.draw_line(340, 324, 340, 355, arcade.csscolor.BLACK, 1)
    # Fenêtre 2 - un rectangle et deux lignes
    dessiner_rectangle(445, 325, 30, 30, arcade.csscolor.WHITE)
    arcade.draw_line(444, 337.5, 475, 337.5, arcade.csscolor.BLACK, 1)
    arcade.draw_line(460, 324, 460, 355, arcade.csscolor.BLACK, 1)


def dessiner_toit(x1, y1, x2, y2, x3, y3, couleur):
    """
    Dessiner le toit en forme de triangle.

    Paramètres:

    - x1: coordonnée x1 angle1 triangle sur l'axe des X.
    - y1: coordonnée y1 angle1 triangle sur l'axe des Y.
    - x2: coordonnée x2 angle2 triangle sur l'axe des X.
    - y2: coordonnée y2 angle2 triangle sur l'axe des Y.
    - x3: coordonnée x3 angle3 triangle sur l'axe des X.
    - y3: coordonnée y3 angle3 triangle sur l'axe des Y.
    - couleur: couleur du triangle.
    """

    arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, couleur)


def dessiner_soleil(centre_x, centre_y, rayon, couleur):
    """
    Dessiner le soleil avec un cercle et les rayons soleil avec des lignes.

    Paramètres:

    - centre_x: centre du cercle sur l'axe des X.
    - centre_y: centre du cercle sur l'axe des Y.
    - rayon: longueur du rayon cercle.
    - couleur: couleur du cercle.
    """

    # Soleil - cercle.
    arcade.draw_circle_filled(centre_x, centre_y, rayon, couleur)

    # Rayons soleil - lignes gauche, droit, haut, bas.
    arcade.draw_line(centre_x, centre_y, centre_x - 75, centre_y, couleur, 3)
    arcade.draw_line(centre_x, centre_y, centre_x + 75, centre_y, couleur, 3)
    arcade.draw_line(centre_x, centre_y, centre_x, centre_y + 75, couleur, 3)
    arcade.draw_line(centre_x, centre_y, centre_x, centre_y - 75, couleur, 3)

    # Rayons soleil - lignes en diagonale.
    arcade.draw_line(centre_x, centre_y, centre_x + 50, centre_y + 50, couleur, 3)
    arcade.draw_line(centre_x, centre_y, centre_x + 50, centre_y - 50, couleur, 3)
    arcade.draw_line(centre_x, centre_y, centre_x - 50, centre_y + 50, couleur, 3)
    arcade.draw_line(centre_x, centre_y, centre_x - 50, centre_y - 50, couleur, 3)


def dessiner_nuage(centre_x, centre_y, largeur, hauteur, couleur):
    """
    Dessiner un nuage avec trois arcs de cercle.

    Paramètres:

    - centre_x: le centre de l'arc sur l'axe des X.
    - centre_y: le centre de l'arc sur l'axe des Y.
    - largeur: la largeur de l'arc.
    - hauteur: l'hauteur de l'arc.
    - couleur: couleur du cercle.
    """

    arcade.draw_arc_filled(centre_x, centre_y, largeur, hauteur, couleur, 0, 180)
    arcade.draw_arc_filled(centre_x - 50, centre_y, largeur, hauteur, couleur, 0, 180)
    arcade.draw_arc_filled(centre_x + 50, centre_y, largeur, hauteur, couleur, 0, 180)


def dessiner_arbres(x, y):
    """
    Dessiner des arbres avec des rectangles, ellipses et polygone.

    Paramètres:

    - x: coordonnée x sur l'axe des X utilisé comme point de reference par rapport aux autres objets.
    - y: coordonnée y sur l'axe des Y utilisé comme point de reference par rapport aux autres objets.
    """

    # Trois arbres avec rectangle comme tronc et ellipse comme feuillage.
    arcade.draw_rectangle_filled(x, y + 20, x / 10, 100, arcade.csscolor.SIENNA)
    arcade.draw_ellipse_filled(x, y + 70, x / 10 * 3, 100, arcade.csscolor.DARK_GREEN)
    arcade.draw_rectangle_filled(x - 50, y + 20, x / 10, 100, arcade.csscolor.SIENNA)
    arcade.draw_ellipse_filled(x - 50, y + 70, x / 10 * 3, 100, arcade.csscolor.DARK_GREEN)
    arcade.draw_rectangle_filled(x + 50, y + 20, x / 10, 100, arcade.csscolor.SIENNA)
    arcade.draw_ellipse_filled(x + 50, y + 70, x / 10 * 3, 100, arcade.csscolor.DARK_GREEN)

    # Un arbre avec rectangle comme tronc et polygon avec une liste de points comme feuillage.
    arcade.draw_rectangle_filled(x + 500, y + 20, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_polygon_filled(((x + 500, 400), (x + 480, y + 40), (x + 470, y + 20),
                               (x + 530, y + 20), (x + 520, y + 40)),
                               arcade.csscolor.DARK_GREEN)


def afficher_texte(x, y, couleur):
    """
    Afficher des textes avec une police et couleur.

    Paramètres:

    - x: coordonnée x de l'emplacement du texte dans la fenêtre.
    - y: coordonnée y de l'emplacement du texte dans la fenêtre.
    """

    # L'information à afficher.
    texte_1 = "TP5 - Alexander Precup, 402"
    texte_2 = "Image avec les fonctions de dessin de la librairie Arcade"
    # Affichage textes.
    arcade.draw_text(texte_1, x, y, couleur, 20, width=SCREEN_WIDTH, align="center")
    arcade.draw_text(texte_2, x, y - 50, couleur, 20, width=SCREEN_WIDTH, align="center")


def main():
    """
    Programme principal.
    """

    # Ouvrir une fenêtre.
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Effacer la fenêtre principale et commencer à dessiner.
    arcade.start_render()

    # Afficher l'arrière-plan.
    dessiner_arriere_plan()

    # Afficher les murs maison.
    dessiner_rectangle(300, 200, 200, 200, arcade.csscolor.DARK_ORANGE)

    # Afficher les fenêtres maison.
    dessiner_fenetres()

    # Afficher la porte maison.
    dessiner_rectangle(375, 200, 50, 100, arcade.csscolor.SIENNA)

    # Afficher le toit maison.
    dessiner_toit(300, 400, 400, 600, 500, 400, arcade.csscolor.MAROON)

    # Afficher la cheminé maison.
    dessiner_rectangle(450, 450, 25, 75, arcade.csscolor.MAROON)

    # Afficher le soleil.
    dessiner_soleil(100, 700, 40, arcade.color.GOLD)

    # Afficher le nuage.
    dessiner_nuage(700, 700, 60, 100, arcade.csscolor.WHITE)

    # Afficher les arbres.
    dessiner_arbres(100, 200)

    # Afficher deux textes de couleur HONEYDEW.
    afficher_texte(15, 100, arcade.csscolor.HONEYDEW)

    # Utiliser le "back buffer" pour afficher la maison.
    arcade.finish_render()

    # Garder la fenêtre ouverte jusqu'à l'usager va la fermer.
    arcade.run()


if __name__ == "__main__":
    main()
