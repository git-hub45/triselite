function closeInventory () {
    inventoryVisible = true
    controller.moveSprite(Player1, 100, 100)
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    selectedIndex = 0
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
	
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    if (inventoryVisible) {
        closeInventory()
    } else {
        openInventory()
    }
})
controller.A.onEvent(ControllerButtonEvent.Repeated, function () {
    currentTile = tiles.locationOfSprite(Player1)
    if (tiles.tileIs(currentTile, assets.tile`myTile0`)) {
        tiles.setTileAt(currentTile, assets.tile`myTile4`)
    }
})
spriteutils.createRenderable(100, function (screen2) {
    let index: number;
let index2: number;
if (inventoryVisible) {
        index = 0
        screen2.fillRect(10, 10, 140, 100, 13)
        screen2.drawRect(10, 10, 140, 100, 15)
        images.print(screen2, "Inventory", 14, 14, 15)
screen2.fillRect(14, 24, 132, 1, 15)
        Tool_top = 28
        index2 = 0
        while (index2 <= Tools.length - 1) {
            spriteutils.drawTransparentImage(Tools[index2], screen2, 14 + index2 * 20, Tool_top)
index2 += 1
        }
        spriteutils.drawTransparentImage(img`
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
            `, screen2, 14 + index * 20, Tool_top)
    }
})
function openInventory () {
    inventoryVisible = true
    controller.moveSprite(Player1, 0, 0)
    selectedIndex = 0
}
let currentTile: tiles.Location = null
let selectedIndex = 0
let inventoryVisible = false
let Player1: Sprite = null
let Tools : Image[] = []
let Tool_top = 0
tiles.setCurrentTilemap(tilemap`level1`)
Player1 = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(Player1)
scene.cameraFollowSprite(Player1)
tiles.placeOnRandomTile(Player1, assets.tile`myTile5`)
tiles.coverAllTiles(
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
        , assets.tile`myTile`)
Tools = [
img`
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
    `,
img`
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
    `,
img`
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
    `,
img`
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
    `
]
let Tool_names = [
"watering pot",
"gloves",
"shovel",
"hoe"
]
