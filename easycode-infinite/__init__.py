from .easycode_addons import (
    PygameVisibleList, 
    PygameVisibleVariable, 
    PygameClickedCalculator,
    PygameHealthBar,
    PygameDraggableSlider,
    PygameScreenShake,
    PygameSmartCamera,
    PygameTextBox,
    PygameDialogueText,
    PygameEasyDraw,
    PygletEasyDraw,
    ArcadeEasyDraw,
    PygameSoundManager,
    get_font,
    change_axis,
    BigString,
    BigDecimal,
    BigVector2,
    BigVector3,
    BigVector4,
    PygameSprite,
    PygameGroup,
    PygameLayeredGroup,
    PygletHealthBar,
    PygletVisibleVariable,
    PygletVisibleList, 
    PygletTextBox,
    PygletDialogueText,
    PygletScreenShake,
    PygletDraggableSlider,
    PygletSprite,
    PygletGroup,
    ArcadeVisibleVariable,
    ArcadeVisibleList,
    ArcadeClickedCalculator,
    ArcadeGUIComponents,
    ArcadeHealthBar,
    ArcadeSprite,
    ArcadeGroup
)

sound = PygameSoundManager()
pg_draw = PygameEasyDraw()
arc_draw = ArcadeEasyDraw()
pgl_draw = PygletEasyDraw()

bigstr    = BigString
bigdec    = BigDecimal
bigvector = BigVector2
bigvector2 = BigVector2
bigvector3 = BigVector3
bigvector4 = BigVector4

pg_sprite  = PygameSprite
pg_group   = PygameGroup
pg_layeredgroup = PygameLayeredGroup
arc_sprite = ArcadeSprite
arc_group  = ArcadeGroup
pgl_sprite = PygletSprite
pgl_group = PygletGroup

__all__ = [
    'PygameVisibleList', 
    'PygameVisibleVariable', 
    'PygameClickedCalculator', 
    'PygameHealthBar',
    'PygameDraggableSlider',
    'PygameSmartCamera',
    'PygameScreenShake',
    'PygameTextBox',
    'PygameDialogueText',
    'PygameEasyDraw',
    'PygletEasyDraw',
    'ArcadeEasyDraw',
    'PygameSoundManager',
    'sound',
    'get_font',
    'change_axis',
    'bigstr', 
    'bigdec', 
    'bigvector', 
    'bigvector2', 
    'bigvector3', 
    'bigvector4',
    'BigString',
    'BigDecimal',
    'BigVector2',
    'BigVector3',
    'BigVector4',
    'PygameSprite',
    'PygameGroup',
    'PygameLayeredGroup',
    'pg_sprite',
    'pg_group',
    'ArcadeSprite',
    'ArcadeGroup',
    'arc_sprite',
    'arc_group',
    'PygletHealthBar', 
    'PygletVisibleVariable',
    'PygletVisibleList', 
    'PygletTextBox',
    'PygletDialogueText',
    'PygletScreenShake',
    'PygletDraggableSlider',
    'PygletSprite',
    'PygletGroup',
    'pgl_sprite',
    'ArcadeVisibleVariable',
    'ArcadeVisibleList',
    'ArcadeClickedCalculator',
    'ArcadeGUIComponents',
    'ArcadeHealthBar'
]

__version__ = "1.0.5"
__author__ = "Kent"