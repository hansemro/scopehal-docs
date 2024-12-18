.. _sec:sdr-drivers:

SDR Drivers
===========

This chapter describes all of the available drivers for software-defined radios.

Ettus Research
--------------

=============  ======  =========  =====
Device Family  Driver  Transport  Notes
=============  ======  =========  =====
USRP           uhd     twinlan

=============  ======  =========  =====

uhd
~~~

This driver connects via a TCP socket to a socket server
`scopehal-uhd-bridge <https://github.com/ngscopeclient/scopehal-uhd-bridge>`_ which connects to the appropriate
instrument using the UHD API.

This provides network transparency for USB-attached instruments, as well as a license boundary between the BSD-licensed
libscopehal core and the GPL-licensed UHD API.

Microphase
----------

The AntSDR running antsdr_uhd firmware is supported by the ``uhd`` driver for Ettus Research SDRs. There is currently no
support for the IIO firmware.
