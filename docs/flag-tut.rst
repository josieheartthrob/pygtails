=====================================
Flags and Bitwise Operations Tutorial
=====================================

A Quick Primer on Flags
-----------------------

If you're unfamiliar with the concept of a flag in the context of computer science, hopefully this is a decent place to start. A flag, in this case, is an integer value that represents a combination of different values. Each value is represented as a power of two, or as a bit of an integer. If we look at the binary representation of an integer, it can be said that for each value in the flag, if the value is "active" it's it's relative "bit" will be represented as a 1. If the value is "inactive" it's relative bit is represented as a 0.

As an example, let's say we have a flag with two possible values; let's say "left" and "right"; let's say "left" is represented by the 2^0 place and "right" is represented by the 2^1 place. The possible flag values can then be represented by the following table:

+------------+------------+------------+
|            | R inactive |  R active  |
+============+============+============+
| L inactive |   00 (0)   |   10 (2)   |
+------------+------------+------------+
| L active   |   01 (1)   |   11 (3)   |
+------------+------------+------------+

Bitwise Operations
------------------
    
Performing operations on flags is usualy done with bitwise operations. Bitwise operations deal with the binary representations of integers. This is perfect for flags because flags are defined by their binary representations.

Combining two or more flag values is usually done with bitwise-OR (|). The result of a bitwise-OR will include a 1 in every place it appeared in any of the combining values. The following are examples of the product of bitwise-OR operations on two integers:::

    8 (1000) | 1 (0001) = 9 (1001)
    6 (0110) | 3 (0011) = 7 (0111)

Checking to see if a flag value is active is usually done with bitwise-AND (&). The result of a bitwise-AND will only have a 1 where both of the combining values are 1. The following are examples of the product of  bitwise-AND operations on two integers:::

    8 (1000) & 1 (0001) = 0 (0000)
    6 (0110) & 3 (0011) = 2 (0010)

Using Bitwise Operations with Flags
-----------------------------------

In the context of pygame, an example of how this can be used is to check if mutliple key mods are down. To check if both ctrl and alt are pressed, you might check the value of the key mod against KMOD_LCTRL | KMOD_LALT. Assuming ``mod`` is the flag value for the current key mods being pressed, a good way to do check if a specific combination is being pressed would look something like:::

    combo = KMOD_LCTRL | KMOD_LALT
    mod & combo == combo

This will perform an inclusive check (other key mods can be pressed as well) to see if ctrl and alt are pressed.::

    KMOD_LCTRL | KMOD_LALT == mod
        
will perform an exclusive check.
