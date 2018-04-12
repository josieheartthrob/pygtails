Hello, Pygtails!
================

This page provides a simple hello world program written with pygtails and a step-by-step breakdown of what's happening.

.. literalinclude:: ../examples/hello.py

Let's start from the beginning

.. code:: python

    import pygame
    from pygtails import Game

.. role:: python(code)
    :language: python

Pygtails is merely an extension of pygame and having pygame installed is a requirement. :python:`import pygame` will import the pygame module.

``pygtails.Game`` is the main class to use to run your pygtails games. :python:`from pygtails import Game` imports the Game class directly into the current namespace so that you don't have to preface ``Game`` with ``pygtails.`` everytime you reference it.

``pygtails.Game`` also saves an instance of a ``pygame.Surface`` object to an attribute named ``screen`` that acts as the main display window for your game. The ``Game`` constructor takes the same arguments as ``pygame.display.set_mode`` and is `documented here`__.

.. _set_mode: https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
__ set_mode_

So :python:`super().__init__((400, 300), "Hello, world!")` uses the ``pygtails.Game`` constructor to create a screen with dimensions 400x300 pixels and with aa title "Hello, world!"

:python:`self.screen.fill((255, 255, 255))` accesses the Surface object that was created in the previous line and fills it with the color white. The most basic specification of ``Surface.fill`` takes a 3-tuple of integers as the RGB values for a color.

Whenever anything is drawn to the screen, it's actually drawn to a sort of buffer screen and changes don't immediately show up. In order to see the changes, we need flush the buffer screen onto the actual screen. To do this we call ``pygame.display.flip()``

.. code:: python

    game = Hello()
    game.main()

Finaly we create an instance of the class we just created and call its main method to run the game. And we're finished! This is the most basic program you can create with pygame and pygtails. To practice using the API, try starting from scratch and creating programs with different sizes, names and background colors without looking at the already written code for reference.
