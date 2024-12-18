.. _sec:powersupply-drivers:

Power Supply Drivers
====================

This chapter describes all of the available drivers for power supplies.

TODO: demo driver

Alientek
--------

=============  ===========  =========  =====
Device Family  Driver       Transport  Notes
=============  ===========  =========  =====
DP100          alientek_dp  hid

=============  ===========  =========  =====

alientek_dp
~~~~~~~~~~~

This driver works on Alientek DP100 mini Digital Power Supply.

Path for connection (vendorId:productId) is: ``2e3c:af01``.

GW Instek
---------

================  =================  =========  =====
Device Family     Driver             Transport  Notes
================  =================  =========  =====
GPD-X303S series  gwinstek_gpdx303s  uart       9600 Baud default. Tested with GPD-3303S. No support for tracking modes yet.

================  =================  =========  =====

gwinstek_gpdx303s
~~~~~~~~~~~~~~~~~

Supported models should include GPD-2303S, GPD-3303S, GPD-4303S, and GPD-3303D.

Kuaiqu
------

====================  ==========  =========  =====
Device Family         Driver      Transport  Notes
====================  ==========  =========  =====
Kuaiqu SSPS-S series  kuaiqu_psu  uart
Kuaiqu SPPS*D series  kuaiqu_psu  uart
Kuaiqu SPPS-D series  kuaiqu_psu  uart       Tested on a Kuaiqu SPPS-D3010-232\\
Kuaiqu R-SPPS series  kuaiqu_psu  uart
====================  ==========  =========  =====

kuaiqu_psu
~~~~~~~~~~

This driver supports all Kuaiqu programmable PSUs, including SSPS-S, SPPS*D, SPPS-D and R-SPPS series.

It has been tested on a Kuaiqu SPPS-D3010-232.

Riden
-----

===============  ===========  =========  =====
Device Family    Driver       Transport  Notes
===============  ===========  =========  =====
Riden RD series  riden_rd     uart       Tested on a Riden RD6006

===============  ===========  =========  =====

riden_rd
~~~~~~~~

This driver supports all Riden RD series DC Power Supplies.

It has been tested on a Riden RD6006.

Rigol
-----

=============  ===========  =================  =====
Device Family  Driver       Transport          Notes
=============  ===========  =================  =====
DP832, DP832A  rigol_dp8xx  uart, usbtmc, lan  No support for tracking modes yet.

=============  ===========  =================  =====

rigol_dp8xx
~~~~~~~~~~~

This driver supports the DP832 and DP832A.

Rohde & Schwarz
---------------

==============  ==========  =================  =====
Device Family   Driver      Transport          Notes
==============  ==========  =================  =====
HMC804x series  rs_hmc804x  uart, usbtmc, lan  No support for tracking modes yet.

==============  ==========  =================  =====

rs_hmc804x
~~~~~~~~~~

This driver should support the HMC8041, HMC8042, and HMC8043 but has only been tested on the HMC8042.

Siglent
-------

===============  ===========  =========  =====
Device Family    Driver       Transport  Notes
===============  ===========  =========  =====
SPD3303X series  siglent_spd  lan        Tested with SPD3303X-E

===============  ===========  =========  =====

siglent_spd
~~~~~~~~~~~

Supported models should include SPD3303X, SPD3303X-E.

NOTE: Channel 3 of the SPD3303x series does not support software voltage/current adjustment. It has a fixed current
limit of 3.2A, and output voltage selectable to 2.5, 3.3, or 5V via a mechanical switch. While channel 3 can be turned
on and off under software control, there is no readback capability whatsoever for channel 3 in the SCPI API.

As a result - regardless of actual hardware state - the driver will report channel 3 as being in constant voltage mode.
Additionally, the driver will report channel 3 as being off until it is turned on by software. Once the output has been
turned on, the driver will track the state and report a correct on/off state as long as no front panel control buttons
are touched.
