.. _sec:funcgen-drivers:

Function Generator Drivers
==========================

This chapter describes all of the available drivers for standalone function generators.

Function generators which are part of an oscilloscope are described in the :ref:`Oscilloscope Drivers <sec:scope-drivers>` section.

Owon
----

====================  ========  ==========  =====
Device Family         Drivers   Transport   Notes
====================  ========  ==========  =====
XDG 2000/3000 series  owon_xdg  lan/usbtmc  Only tested via lan transport, but USBTMC is available too.

====================  ========  ==========  =====

owon_xdg
~~~~~~~~

This driver supports all XDG 2000/3000 series function / arbitrary waveform generators.

It has been tested on an Owon XDG 2035.

The default communication port for lan is 3000.

Rigol
-----

=============  =========  ==========  =====
Device Family  Drivers    Transport   Notes
=============  =========  ==========  =====
DG4000 series  rigol_awg  lan         Only tested via lan transport, but USBTMC and serial are available too

=============  =========  ==========  =====

rigol_awg
~~~~~~~~~

This driver supports all DG4000 series function / arbitrary waveform generators.

Siglent
-------

===============  ===========  ==========  =====
Device Family    Drivers      Transport   Notes
===============  ===========  ==========  =====
SDG2000X series  siglent_awg  lan         Only tested via lan transport, but USBTMC is available too

===============  ===========  ==========  =====

siglent_awg
~~~~~~~~~~~

This driver supports the SDG2000X series and possibly higher end models as well.
