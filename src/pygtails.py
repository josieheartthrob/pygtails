"""A simple wrapper around pygame.

Game        implements engine functionality. Subclass to build games.
GameObject  A simple class to provide a more intuitive approach to gamedev.

Pygame Constants

    One of the reasons I decided to create this little library is because I
    feel that pygame isn't very well documented. Part of this is attributed to
    poor organization (in my opinion) of documentation of related data types
    and functions. This documentation aims to remedy that by putting the
    documentation in a visible spot to be easy to reference.

The following table is almost directly from the pygame documentation.

Keycodes

    Pygame name     ascii   description
    K_BACKSPACE     \\b     backspace
    K_TAB           \\t     tab
    K_CLEAR                 clear
    K_RETURN        \\r     return
    K_PAUSE                 pause
    K_ESCAPE        ^[      escape
    K_SPACE                 space
    K_EXCLAIM       !       exlclamation point
    K_QUOTEDBL      "       double quote
    K_HASH          #       hashtag
    K_DOLLAR        $       dollar sign
    K_AMPERSAND     &       ampersand
    K_QUOTE         '       single quote
    K_LEFTPAREN     (       opening parenthesis
    K_RIGHTPAREN    )       closing parenthesis
    K_ASTERISK      *       asterisk
    K_PLUS          +       plus
    K_COMMA         ,       comma
    K_MINUS         -       hyphen
    K_PERIOD        .       period
    K_SLASH         /       forward slash
    K_0             0       0
    K_1             1       1
    K_2             2       2
    K_3             3       3
    K_4             4       4
    K_5             5       5
    K_6             6       6
    K_7             7       7
    K_8             8       8
    K_9             9       9
    K_COLON         :       colon
    K_SEMICOLON     ;       semicolon
    K_LESS          <       less-than
    K_EQUALS        =       equals
    K_GREATER       >       greater-than
    K_QUESTION      ?       question mark
    K_AT            @       at sign
    K_LEFTBRACKET   [       opening sqaure bracket
    K_BACKSLASH     \\      backslash
    K_RIGHTBRACKET  ]       closing right bracket
    K_CARET         ^       caret
    K_UNDERSCORE    _       underscore
    K_BACKQUOTE     `       backtick
    K_a             a       a
    K_b             b       b
    K_c             c       c
    K_d             d       d
    K_e             e       e
    K_f             f       f
    K_g             g       g
    K_h             h       h
    K_i             i       i
    K_j             j       j
    K_k             k       k
    K_l             l       l
    K_m             m       m
    K_n             n       n
    K_o             o       o
    K_p             p       p
    K_q             q       q
    K_r             r       r
    K_s             s       s
    K_t             t       t
    K_u             u       u
    K_v             v       v
    K_w             w       w
    K_x             x       x
    K_y             y       y
    K_z             z       z
    K_DELETE                delete
    K_KP0                   numpad 0
    K_KP1                   numpad 1
    K_KP2                   numpad 2
    K_KP3                   numpad 3
    K_KP4                   numpad 4
    K_KP5                   numpad 5
    K_KP6                   numpad 6
    K_KP7                   numpad 7
    K_KP8                   numpad 8
    K_KP9                   numpad 9
    K_KP_PERIOD     .       numpad period
    K_KP_DIVIDE     /       numpad divide
    K_KP_MULTIPLY   *       numpad multiply
    K_KP_MINUS      -       numpad minus
    K_KP_PLUS       +       numpad plus
    K_KP_ENTER      \\r     numpad enter
    K_KP_EQUALS     =       numpad equals
    K_UP                    up arrow
    K_DOWN                  down arrow
    K_RIGHT                 right arrow
    K_LEFT                  left arrow
    K_INSERT                insert
    K_HOME                  home
    K_END                   end
    K_PAGEUP                page up
    K_PAGEDOWN              page down
    K_F1                    F1
    K_F3                    F3
    K_F4                    F4
    K_F5                    F5
    K_F6                    F6
    K_F7                    F8
    K_F9                    F9
    K_F10                   F10
    K_F11                   F11
    K_F12                   F12
    K_F13                   F13
    K_F14                   F14
    K_F15                   F15
    K_NUMLOCK               num lock
    K_CAPSLOCK              caps lock
    K_SCROLLOCK             scroll lock
    K_RSHIFT                right shift
    K_LSHIFT                left shift
    K_RCTRL                 right control
    K_LCTRL                 left control
    K_RALT                  right alt
    K_LALT                  left alt
    K_RMETA                 right meta
    K_LMETA                 left meta
    K_LSUPER                left "windows" key
    K_RSUPER                right "windows" key
    K_MODE                  mode shift
    K_HELP                  help
    K_PRINT                 print screen
    K_SYSREQ                sysrq
    K_BREAK                 break
    K_MENU                  menu
    K_POWER                 power
    K_EURO                  euro

Pygame Flags

A Quick Primer on Flags

    If you're unfamiliar with the concept of a flag in the context of computer
    science, hopefully this is a decent place to start. A flag, in this case,
    is an integer value that represents a combination of different values.
    Each value is represented as a power of two, or as a bit of an integer.
    If we look at the binary representation of an integer, it can be said that
    for each value in the flag collection, if the value is "active" it's
    represented as a 1. If the value is "inactive" it's represented as a 0.

    As an example, let's say we have a flag with two possible values; let's
    say "left" and "right"; let's say "left" is represented by the 2^0 place
    and "right" is represented by the 2^1 place. The possible flag values can
    then be represented by the following table:

               | R inactive |  R active  |
    --------------------------------------
    L inactive |   00 (0)   |   10 (2)   |
    L active   |   01 (1)   |   11 (3)   |
    
    Combining of flags is usualy done with bitwise operations, specifically
    bitwise OR (|). Bitwise OR works similarly to boolean or. When combining
    two or more values via bitwise-OR, every 1 that appears in the binary
    representation will appear in the result.

    e.g.    8 (1000) | 1 (0001) = 9 (1001)
            6 (0110) | 3 (0011) = 7 (0111)

    In the context of pygame, an example of how this can be used is to check
    if mutliple key mods are down. To check if both ctrl and alt are pressed,
    you might check the value of the key mod against KMOD_CTRL | KMOD_ALT.
    A good way to do this is probably something like

        mod | (KMOD_CTRL | KMOD_ALT) == mod

    This will perform a inclusive check (other key mods can be pressed as well)
    to see if ctrl and alt are pressed.

        KMOD_CTRL | KMOD_ALT == mod
        
    will perform an exclusive check.

Key Mod Flags

"""
#TODO: better documentation for pygame keycodes, key mod flags, and display
#      mode flags

import pygame
import sys

from pygame.time import Clock
from pygame.event import Event

class Game(object):
    
    """A class that handles pygame events, input, and mouse-collision.

    Pubic Methods:

    main, quit, on_focus, on_key_down, on_key_up, on_mouse_move, on_mouse_up,
    on_mouse_down, on_resize, update, add_object, destroy_object, key_is_pressed

    Instance variables:

    screen

    """

    def __init__(self, resolution, title, flags=0, depth=0):
        """Create a new game with a blank window.
        
        Positional Arguments:

        resolution      A 2-tuple of integers specifying the width and
                        height of the screen.

        title           A string that will be used as the title of the
                        window.
        
        Keyword Arguments:

        flags           An integer value representing the the diferent
                        controls over the display mode. For more detailed
                        information, see the module documentation on pygame
                        display mode flags.
        """
        pygame.init() 
        self._screen = pygame.display.set_mode(resolution, flags, depth)
        pygame.display.set_caption(title)

        self._cur_id = 0
        self._objects = {}
        self._contains_mouse = {}
        self._clicked = {}

        self._keys_pressed = pygame.key.get_pressed()

        self._handle = {pygame.QUIT:            self.quit,
                        pygame.ACTIVEEVENT:      self.on_focus,
                        pygame.KEYDOWN:         self.on_key_down,
                        pygame.KEYUP:           self.on_key_up,
                        pygame.MOUSEMOTION:     self.on_mouse_move,
                        pygame.MOUSEBUTTONUP:   self.on_mouse_up,
                        pygame.MOUSEBUTTONDOWN: self.on_mouse_down,
                        pygame.VIDEORESIZE:     self.on_resize}

    def main(self):
        """The main loop. Call this to run the game."""
        while True:
            for event in pygame.event.get():
                self._handle[event.type](event)

            self._keys_pressed = pygame.key.get_pressed()
            buttons = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            rel = pygame.mouse.get_rel()

            event = Event(pygame.MOUSEMOTION, buttons=buttons,
                          pos=pos, rel=rel)
            for obj in self._contains_mouse.values():
                obj.on_mouse_stay(event)

            self.update()
            for obj in self._objects.values():
                obj.update()

    def quit(self, event):
        """The method called when the exit button is pressed.

        Positional Arguments (passed implicitly):

        event   A pygame QUIT event. Has no event attributes.
        
        This method is predefined as
        
        pygame.quit()
        sys.exit()
        
        Redefine it if you need more control.
        """
        pygame.quit()
        sys.exit()

    def on_focus(self, event):
        """This method is called whenever the game window loses or gains focus.

        Positional Arguments (passed implicitly):

        event       A pygame ACTIVEEVENT event. Contains event attributes:

          gain      An integer. Has a value of 1 when the window comes
                    into focus or when the mouse enters the window. Has a
                    value of 0 when the window goes out of focus or when the
                    mouse leaves the window.

          state     An integer. Has a value of 1 when the mouse exits or
                    leaves the window. Has a value of 2 when the window
                    gains or loses focus.

        This method is not predefined.
        """
        pass

    def on_key_down(self, event):
        """This method is called whenever a key is pressed.
        
        Positional Arguments (passed implicitly):

        event       A pygame KEYDOWN event. contains the event attributes:

          unicode   The unicode value that was pressed.

          key       An integer value represinting the key being pressed. The
                    corresponding character is defined by pygame.locals
                    variables prefaced with K_. For a more in-depth
                    explanation of these, see the pygame documentation
                    section for pygame keycodes.

          mod       An integer flag value representing the total "modulation"
                    (shift, ctrl, alt, etc.) keys being pressed when the
                    current key was pressed. The possible flags are defined by
                    pygame.locals variables prefaced with KMOD_. For more in-
                    depth explanation of these, see the module documentation
                    for pygame key mod flags.

        This method is not predefined.
        """
        pass

    def on_key_up(self, event):
        """This method is called whenever a key is released.

        Positional Arguments (passed implicitly):

        event   A pygame KEYUP event. contains the event attributes:

          key   An integer value representing the key being released. The
                corresponding character is defined by pygame.locals variables
                prefaced with K_. For more in-depth explanation of these, see
                th module documentation for pygame keycodes.

          mod   An integer flag value representing the total "modulation"
                (shit, ctrl, alt, etc.) keys being pressed when the current
                key was released. The possible flags are defined by
                pygame.locals variables prefaced with KMOD_. For a more in-
                depth explanation of thses, see the module documentation for
                pygame key mod flags.

        This method is not predefined.
        """
        pass

    def on_mouse_move(self, event):
        """This method is called whenever the mouse is moved.

        Positional Arguments (passed implicitly):

        event       A pygame MOUSEMOTION event. Contains the event attributes:
          
          pos       A 2-tuple of integers representing the x and y coordinates
                    of the mouse.

          rel       A 2-tuple of integers representing the change in x and y
                    since the last time this function was called.

          buttons   A 3-tuple of integers representing the amount of mouse
                    buttons being pressed. Index 0 represents the left mouse
                    button, 1 represents the middle mouse button, 2 represents
                    the right mouse button. If the mouse button is down, the
                    value is 1, 0 if it's up.

        This method is predefined to implement the on_mouse_[enter, exit, drag]
        functions.
        
        If you aren't satisfied with the implementation, feel free
        to redefine it. If you want to keep the implementation but also add
        additional functionality call super().on_mouse_move(event) when you're
        redefining the function.
        """
        #TODO: Add support for sleeping vs awake objects
        for ID, obj in self._objects.items():
            mouse_is_colliding = obj.is_colliding_with(event.pos)
            if not obj._contains_mouse and mouse_is_colliding:
                self._contains_mouse[ID] = obj
                obj._contains_mouse = True
                obj.on_mouse_enter(event)
            elif obj._contains_mouse and not mouse_is_colliding:
                del self._contains_mouse[ID]
                obj._contains_mouse = False
                obj.on_mouse_exit(event)

        for obj in self._clicked.values():
            obj.on_mouse_drag(event)

    def on_mouse_up(self, event):
        """This method is called whenever a mouse button is released.

        Positional Arguments (passed implicitly):

        event       A pygame MOUSEBUTTONUP event. Contains the attributes:

          pos       A 2-tuple of integers representing the x and y coordinates
                    of the mouse when it was released.

          button    An integer representing the button being released. 1
                    represents the left mouse button, 2 represents the middle
                    mouse button, and 3 represents the right mouse button.

        This method is predefined to implement the GameObject.on_mouse_up
        method and to update internal data about whether or not an object is
        clicked.

        To redefine this method while keeping the implementation call
        super().on_mouse_up(event) at the top of your function.
        """
        if event.button == 1:
            for obj in self._clicked.values():
                obj.on_mouse_up(event)
            self._clicked.clear()

    def on_mouse_down(self, event):
        """This method is called whenever a mouse button is pressed.

        Positional Arguments (passed implicitly):

        event       A pygame MOUSEBUTTONDOWN event. Contains the attributes:

          pos       A 2-tuple of integers representing the x and y coordinates
                    of the mouse when it was pressed.

          button    An integer representing the button being pressed. 1
                    represents the left mouse button, 2 represents the middle
                    mouse button, and 3 represents the right mouse button.

        This method is predefined to implement the GameObject.on_mouse_down
        method and to update internal data bout whether or not an object is
        clicked.

        To redefine this method while keeping the implementation, call
        super().on_mouse_up(event) at the top of your function.
        """
        if event.button == 1:
            for obj in self._contains_mouse.values():
                obj.on_mouse_down(event)
            self._clicked.update(self._contains_mouse)

    def on_resize(self, event):
        """This method is called whenever the window is resized.
        
        Positional Arguments (passed implicitly):

        event       A pygame VIDEORESIZE event. Contains the attributes:

          size      A 2-tuple of integers representing the width and height
                    of the screen.

          w         An integer representing the width of the screen.

          h         An integer representing the height of the screen.

        This method is not predefined.
        """
        pass

    def update(self):
        """This method is called every frame.

        This method is not predefined.
        """
        pass

    def add_object(self, other):
        """Add an object to the Game.

        Positional Arguments:

        other   The object to add to the game. The object must either be a
                pygtails.GameObject or implement a specific list of functions
                and attributes.

        Post Conditions:

        returns         The object id

        side-effects    Adds an the given object to the Games inner list of
                        objects. Changes the game's inner current id.
        """
        # TODO: provide full documentation for the functions and attributes
        #       to implement

        obj_id = self.cur_id
        self._objects[obj_id] = obj
        self.cur_id += 1
        return obj_id

    def destroy_object(self, _id):
        """Destroys the object with the given id from the game.

        Note: Does not "undraw" the object. This must be done manually (for now)
        """
        del self._objects[_id]
        for name in ("contains_mouse", "clicked"):
            D = getattr(self, "_"+name)
            if _id in D: del D[_id]

    def key_is_pressed(self, key):
        """Determine if a key is pressed.

        Positional Arguments:

        key     A pygame key constant (pygame.locals variable starting with K_)

        Postconditions:

        returns True if the specified key is pressed, False if not.
        """
        return self._keys_pressed[key]

    @property
    def screen(self):
        """The pygame Surface used to draw and blit images to the screen."""
        return self._screen

class GameObject(object):

    """A simple class to make game development with pygame more intuitive.

    Public Methods:

    is_colliding_with, update, on_mouse_enter, on_mouse_exit, on_mouse_stay,
    on_mouse_down, on_mouse_up, on_mouse_drag, move

    Instance Variables:

    game, ID, position, x, y

    """

    def __init__(self, game, position):
        """Create a new GameObject

        Positional Arguments:

        game        The pygame.Game object that this GameObject will be
                    added to.

        position    A 2-tuple of integers representing the x and y coordinates
                    of the object.
        """
        self._game = game
        self._x, self._y = position
        self._position = position
        self._contains_mouse = False

        self._id = game.add_object(self)

    def is_colliding_with(self, other):
        """Return true if other is colliding with this object.

        Positional Arguments:

        other       A geometric object on the same plane as this object. The
                    type of the object is specifically not specified, as this
                    method is meant to support collision detection for multiple
                    different types of objects determined by its implementation.
                    Must implement collision with a 2D point (tuple).

        Postconditions:

        Returns a boolean value, True if other is colliding with this object,
        False if not.

        This method is not implemented on the GameObject level.
        """
        pass

    def update(self):
        """This method is called every frame.

        This method is not predefined.
        """
        pass

    def on_mouse_enter(self, event):
        """This method is called whenever the mouse enters this object.

        Positional Arguments (passed implicitly):

        event       A pygame MOUSEMOTION event. Contains the event attributes:
          
          pos       A 2-tuple of integers representing the x and y coordinates
                    of the mouse.

          rel       A 2-tuple of integers representing the change in x and y
                    since the last time this function was called.

          buttons   A 3-tuple of integers representing the amount of mouse
                    buttons being pressed. Index 0 represents the left mouse
                    button, 1 represents the middle mouse button, 2 represents
                    the right mouse button. If the mouse button is down, the
                    value is 1, 0 if it's up.

        This method is not predefined.
        """
        pass

    def on_mouse_exit(self, event):
        """This method is called whenever the mouse exits this object.

        Positional Arguments (passed implicitly):

        event       A pygame MOUSEMOTION event. Contains the event attributes:
          
          pos       A 2-tuple of integers representing the x and y coordinates
                    of the mouse.

          rel       A 2-tuple of integers representing the change in x and y
                    since the last time this function was called.

          buttons   A 3-tuple of integers representing the amount of mouse
                    buttons being pressed. Index 0 represents the left mouse
                    button, 1 represents the middle mouse button, 2 represents
                    the right mouse button. If the mouse button is down, the
                    value is 1, 0 if it's up.

        This method is not predefined.
        """
        pass

    def on_mouse_stay(self, event):
        """This method is called each frame the mouse is within this object.

        Positional Arguments (passed implicitly):

        event       A mock pygame MOUSEMOITION event. Contains attributes:

          pos       A 2-tuple of integers representing the x and y coordinates
                    of the mouse.

          rel       A 2-tuple of integers representing the change in x and y
                    since the last time this function was called.

          buttons   A 3-tuple of integers representing the amount of mouse
                    buttons being pressed. Index 0 represents the left mouse
                    button, 1 represents the middle mouse button, 2 represents
                    the right mouse button. If the mouse button is down, the
                    value is 1, 0 if it's up.

        This method is not predefined.
        """
        pass

    def on_mouse_down(self, event):
        """This method is called when the mouse is pressed inside this object.

        Positional Arguments (passed implicitly):

        event       A pygame.MOUSEBUTTONDOWN event. Contains event attributes:

          pos       A 2-tuple of integers representing the x and y coordinates
                    of the mouse when it was pressed.

          button    An integer representing the button being pressed. 1
                    represents the left mouse button, 2 represents the middle
                    mouse button, and 3 represents the right mouse button.

        This method is not predefined.
        """
        pass

    def on_mouse_up(self, event):
        """This method is called on mouse up if this object is clicked.

        Positional Arguments (passed implicitly):

        event       A pygame MOUSEBUTTONUP event. Contains the attributes:

          pos       A 2-tuple of integers representing the x and y coordinates
                    of the mouse when it was released.

          button    An integer representing the button being released. 1
                    represents the left mouse button, 2 represents the middle
                    mouse button, and 3 represents the right mouse button.

        This method is not predefined.
        """
        pass

    def on_mouse_drag(self, event):
        """This method is called each frame this object is dragged by the mouse.

        Positional Arguments (passed implicitly):

        event       A pygame MOUSEMOTION event. Contains the event attributes:
          
          pos       A 2-tuple of integers representing the x and y coordinates
                    of the mouse.

          rel       A 2-tuple of integers representing the change in x and y
                    since the last time this function was called.

          buttons   A 3-tuple of integers representing the amount of mouse
                    buttons being pressed. Index 0 represents the left mouse
                    button, 1 represents the middle mouse button, 2 represents
                    the right mouse button. If the mouse button is down, the
                    value is 1, 0 if it's up.

        This method is not predefined.
        """
        pass

    def move(self, dx, dy):
        """Move the object by the given dimensions.  
        Positional Arguments:
        
        dx  The change in the x-axis. An integer.
        dy  The change in the y-axis. An integer.

        Post Conditions:

        Changes the object's x, y, and position attributes.
        """
        self._x += dx
        self._y += dy
        self._position = (self._x, self._y)

    @property
    def game(self):
        """The pygtails.Game object that this object is a part of."""
        return self._game

    @property
    def ID(self):
        """The id of the game object (An integer)."""
        return self._id

    @property
    def position(self):
        """The position of the game object.

        A 2-tuple of integers representing the x and y cooridnates

        Setting this will change the object's x, y, and position attributes.
        """
        return self._position
    @position.setter
    def position(self, other):
        self._x, self._y = other
        self._positon = other

    @property
    def x(self):
        """The x position of the game object (An integer).
        
        Setting this will change the object's x and position attributes.
        """
        return self._x
    @x.setter
    def x(self, other):
        self._x = other
        self._position = (self._x, self._y)

    @property
    def y(self):
        """The y position of the game object (An integer).
        
        Setting this will change the object's y and position attributes.
        """
        return self._y
    @y.setter
    def y(self, other):
        self._y = other
        self._posiiton = (self._x, self._y)
