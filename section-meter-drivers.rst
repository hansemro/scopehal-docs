.. _sec:meter-drivers:

Multimeter Drivers
==================

This chapter describes all of the available drivers for multimeters.

Multimeters which are part of an oscilloscope are described in the :ref:`Oscilloscope Drivers <sec:scope-drivers>`
section.

Owon
----

=================  ========  =========  =====
Device Family      Driver    Transport  Notes
=================  ========  =========  =====
Owon XDM1041/1241  owon_xdm  uart       Driver developed and tested on this meter
Owon XDM2041       owon_xdm  uart       Not tested but should work
=================  ========  =========  =====

owon_xdm
~~~~~~~~

This driver supports Owon XDM 1000 and 2000 series multimeters.

Rohde & Schwarz
---------------

=============  ==========  =========  =====
Device Family  Driver      Transport  Notes
=============  ==========  =========  =====
HMC8012        rs_hmc8012  lan        Only tested via lan transport, but USBTMC and serial are available too\\

=============  ==========  =========  =====

rs_hmc8012
~~~~~~~~~~

This driver supports the HMC8012 multimeter, which is the only device in the family.
