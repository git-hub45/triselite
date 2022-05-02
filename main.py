def closeInventory():
    global inventoryVisible
    inventoryVisible = True
    controller.move_sprite(Player1, 100, 100)

def on_left_pressed():
    global selectedIndex
    selectedIndex = 0
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    pass
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_menu_pressed():
    if inventoryVisible:
        closeInventory()
    else:
        openInventory()
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def on_a_repeated():
    global currentTile
    currentTile = tiles.location_of_sprite(Player1)
    if tiles.tile_is(currentTile, assets.tile("""
        myTile0
    """)):
        tiles.set_tile_at(currentTile, assets.tile("""
            myTile4
        """))
controller.A.on_event(ControllerButtonEvent.REPEATED, on_a_repeated)

def openInventory():
    global inventoryVisible, selectedIndex
    inventoryVisible = True
    controller.move_sprite(Player1, 0, 0)
    selectedIndex = 0

def on_create_renderable(screen2):
    global Tool_top
    if inventoryVisible:
        index = 0
        screen2.fill_rect(10, 10, 140, 100, 13)
        screen2.draw_rect(10, 10, 140, 100, 15)
        images.print(screen2, "Inventory", 14, 14, 15)
        screen2.fill_rect(14, 24, 132, 1, 15)
        Tool_top = 28
        index2 = 0
        while index2 <= len(Tools) - 1:
            spriteutils.draw_transparent_image(Tools[index2], screen2, 14 + index2 * 20, Tool_top)
            index2 += 1
        spriteutils.draw_transparent_image(img("""
                ff11ffffffffffff11ff
                            f..................f
                            1..................1
                            1..................1
                            f..................f
                            f..................f
                            f..................f
                            1..................1
                            1..................1
                            1..................1
                            1..................1
                            1..................1
                            1..................1
                            f..................f
                            f..................f
                            f..................f
                            1..................1
                            1..................1
                            f..................f
                            ff11ffffffffffff11ff
            """),
            screen2,
            14 + index * 20,
            Tool_top)
spriteutils.create_renderable(100, on_create_renderable)

Tool_top = 0
currentTile: tiles.Location = None
selectedIndex = 0
inventoryVisible = False
Tools: List[Image] = []
Player1: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
"""))
Player1 = sprites.create(img("""
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 1 9 9 9 9 9 9 9 9 1 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 1 9 9 9 9 9 9 9 9 1 9 9 9 
            9 9 9 1 9 9 9 9 9 9 9 9 1 9 9 9 
            9 9 9 1 9 9 9 9 9 9 9 9 1 9 9 9 
            9 9 9 1 9 9 9 9 9 9 9 9 1 9 9 9 
            9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    """),
    SpriteKind.player)
controller.move_sprite(Player1)
scene.camera_follow_sprite(Player1)
tiles.place_on_random_tile(Player1, assets.tile("""
    myTile5
"""))
tiles.cover_all_tiles(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    assets.tile("""
        myTile
    """))
Tools = [img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . 6 
            . . . . 6 6 6 6 6 6 . . . . . 6 
            . . . 6 9 9 9 9 9 9 6 . . . 6 6 
            . . . 6 6 6 6 6 6 6 6 . . 6 9 6 
            . . 6 6 6 6 6 6 6 6 6 . 6 9 . 6 
            . 6 . 6 6 6 6 6 6 6 6 6 9 . . 6 
            . 6 . 6 6 6 6 6 6 6 6 9 . . . . 
            . 6 . 6 6 6 6 6 6 6 6 . . . . . 
            . 6 . 6 6 6 6 6 6 6 6 . . . . . 
            . 6 . 6 6 6 6 6 6 6 6 . . . . . 
            . . 6 6 6 6 6 6 6 6 6 . . . . . 
            . . . 6 6 6 6 6 6 6 6 . . . . . 
            . . . 6 6 6 6 6 6 6 6 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    img("""
        . . . . . . . . . . . . . . . . 
            . . b b b b . . . . . . . . . . 
            . b b 1 1 1 b . . . . . . . . . 
            . b 1 1 1 1 1 b . . . . . . . . 
            . b 1 1 1 1 1 b . . . . . . . . 
            . b 1 1 1 b b b . . . . . . . . 
            . . b 1 1 b e . . . . . . . . . 
            . . . b b b 4 e . . . . . . . . 
            . . . . . . . 4 e . . . . . . . 
            . . . . . . . . 4 e . . . . . . 
            . . . . . . . . . 4 e . . . . . 
            . . . . . . . . . . 4 e . . . . 
            . . . . . . . . . . . 4 e . . . 
            . . . . . . . . . . . . 4 e . . 
            . . . . . . . . . . . . . 4 e . 
            . . . . . . . . . . . . . . 4 e
    """),
    img("""
        . . . . . b b b . . . . . . . . 
            . . . . b 1 1 b . . . . . . . . 
            . . . b 1 1 b . . . . . . . . . 
            . . b b 1 b . . . . . . . . . . 
            . . b 1 1 b . . . . . . . . . . 
            . . b b 4 e . . . . . . . . . . 
            . . . . . 4 e . . . . . . . . . 
            . . . . . . 4 e . . . . . . . . 
            . . . . . . . 4 e . . . . . . . 
            . . . . . . . . 4 e . . . . . . 
            . . . . . . . . . 4 e . . . . . 
            . . . . . . . . . . 4 e . . . . 
            . . . . . . . . . . . 4 e . . . 
            . . . . . . . . . . . . 4 e . . 
            . . . . . . . . . . . . . 4 e . 
            . . . . . . . . . . . . . . 4 e
    """),
    img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . f f f f f f f . . . . 
            . . . . . f f f f f f f . . . . 
            . . . . . f 9 f 9 f 9 f . . . . 
            . . . . . f 9 f 9 f 9 f . . . . 
            . . . . . f 9 f 9 f 9 f . . . . 
            . . . f f f 9 f 9 f 9 f . . . . 
            . . . f 9 f 9 f 9 f 9 f . . . . 
            . . . f 9 f 9 f 9 f 9 f . . . . 
            . . . f f f f f f f f f . . . . 
            . . . . . . f f f f f . . . . . 
            . . . . . . f f f f f . . . . . 
            . . . . . . f f f f f . . . . . 
            . . . . . . f f f f f . . . . . 
            . . . . . . . . . . . . . . . .
    """)]
Tool_names = ["watering pot", "gloves", "shovel", "hoe"]