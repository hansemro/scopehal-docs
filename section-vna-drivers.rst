.. _sec:vna-drivers:

VNA Drivers
===========

This chapter describes all of the available drivers for vector network analyzers.

Copper Mountain
---------------

=============  ========  =========  =====
Device Family  Driver    Transport  Notes
=============  ========  =========  =====
Planar         coppermt  lan        Not tested, but docs say same command set
S5xxx          coppermt  lan        Tested on S5180B
S7530          coppermt  lan        Not tested, but docs say same command set
SC50xx         coppermt  lan        Not tested, but docs say same command set
C1xxx          coppermt  lan        Not tested, but docs say same command set
C2xxx          coppermt  lan        Not tested, but docs say same command set
C4xxx          coppermt  lan        Not tested, but docs say same command set
M5xxx          coppermt  lan        Not tested, but docs say same command set
=============  ========  =========  =====

coppermt
~~~~~~~~

This driver supports the S2VNA and S4VNA software from Copper Mountain.

As of this writing, only 2-port VNAs are supported. 4-port VNAs will probably work using only the first two ports,
but this has not been tested.

NanoVNA
-------

=============  ========  =========  =====
Device Family  Driver    Transport  Notes
=============  ========  =========  =====
NanoVNA        nanovna   uart       Not tested but should work
NanoVNA-D      nanovna   uart       Not tested but should work
NanoVNA-F      nanovna   uart       Not tested but should work
DeepVNA 101    nanovna   uart       Development and tests made on this device (a.k.a. NanoVNA-F Deepelec)
NanoVNA-F_V2   nanovna   uart       Not tested but should work
NanoVNA-H      nanovna   uart       Not tested but should work
NanoVNA-H4     nanovna   uart       Not tested but should work
=============  ========  =========  =====

nanovna
~~~~~~~

This driver supports the NanoVNA with different variants of the original design and firmware (see above).

Communication with the device uses UART transport layer with a connection string looking like this (DTR flag is required):

.. code-block::

    COM6:115200:DTR

Paginated sweep has been implemented to achieve memory depths greater then the device's internal limit.

Pagination is also used at low RBW to prevent the connection from timing out during sweep.

NanoVNA V2 (with binary protocol) is NOT supported.

Pico Technology
---------------

=============  ========  =========  =====
Device Family  Driver    Transport  Notes
=============  ========  =========  =====
PicoVNA 106    picovna   lan
PicoVNA 108    picovna   lan
=============  ========  =========  =====

picovna
~~~~~~~

This driver supports the PicoVNA 5 software from Pico Technology. The older PicoVNA 3 software does not provides a SCPI
interface and is not compatible with this driver.
