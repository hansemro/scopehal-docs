.. _sec:scope-drivers:

Oscilloscope Drivers
====================

This chapter describes all of the available drivers for oscilloscopes and logic analyzers.

Agilent
-------

Agilent devices support a similar similar SCPI command set across most device families.

Please see the table below for details of current hardware support:

========================  =======  =========  =====
Device Family             Driver   Transport  Notes
========================  =======  =========  =====
DSO5000 series            agilent  lan        Not recently tested, but should work.
DSO6000 & MSO6000 series  agilent  lan        Working. No support for digital channels yet.
DSO7000 & MSO7000 series  agilent  lan        Untested, but should work. No support for digital channels yet.
EDUX1000 series           agilent  lan        Untested but should be identical to DSOX1200 but with lower sample memory.
DSOX1200 series           agilent  lan        Working. No support for wavegen yet.
MSOX-2000 series          agilent  lan
MSOX-3000 series          agilent  lan
========================  =======  =========  =====

agilent
~~~~~~~

Typical Performance (MSO6034A, LAN)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Interestingly, performance sometimes gets better with more channels or deeper memory. Not sure why.

========  ============  =====
Channels  Memory depth  WFM/s
========  ============  =====
1         1K            66
4         1K            33
4         4K            33
1         40K           33
1         4K            22
1         20K           22
4         20K           22
1         100K          22
4         10K           17
4         40K           12
1         200K          11
1         400K          8
4         100K          6.5
4         200K          4
1         1M            3.7
4         400K          2.3
1         1M            1
4         1M            1
4         4M            0.2
========  ============  =====

Typical Performance (MSOX3104T, LAN)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ============  =====
Channels  Memory depth  WFM/s
========  ============  =====
1         2.5K          3.3
4         2.5K          2.5
1         2.5M          1.0
4         2.0M          0.5
========  ============  =====

Antikernel Labs
---------------

==============================  =======  =====
Device Family                   Driver   Notes
==============================  =======  =====
Internal Logic Analyzer IP      akila
BLONDEL Oscilloscope Prototype  aklabs
==============================  =======  =====

akila
~~~~~

This driver uses a raw binary protocol, not SCPI.

Under-development internal logic analyzer analyzer core for FPGA design debug. The ILA uses a UART interface to a host
system. Since there's no UART support in scopehal yet, socat must be used to bridge the UART to a TCP socket using
the "lan" transport.

aklabs
~~~~~~

This driver uses two TCP sockets. Port 5025 is used for SCPI control plane traffic, and port 50101 is used for waveform
data using a raw binary protocol.

Demo
----

The ``demo`` driver is a simulation-only driver for development and training purposes, and does not connect to real
hardware.

It ignores any transport provided, and is normally used with the ``null`` transport.

The demo instrument is intended to illustrate the usage of ngscopeclient for various types of analysis and to aid in
automated testing on computers which do not have a connection to a real oscilloscope, and is not intended to accurately
model the response or characteristics of real world scope frontends or signals.

It supports memory depths of 10K, 100K, 1M, and 10M points per waveform at rates of 1, 5, 10, 25, 50, and 100 Gsps.
Four test signals are provided, each with 10 mV of Gaussian noise and a 5 GHz low-pass filter added (although this can
be disabled under the channel properties)

Test signals:

*   1.000 GHz tone
*   1.000 GHz tone mixed with a second tone, which sweeps from 1.100 to 1.500 GHz
*   10.3125 Gbps PRBS-31
*   1.25 Gbps repeating two 8B/10B symbols (K28.5 D16.2)

========================  =======  =========  =====
Device Family             Driver   Transport  Notes
========================  =======  =========  =====
Simulator                 demo     null

========================  =======  =========  =====

Digilent
--------

Digilent oscilloscopes using the WaveForms SDK are all supported using the ``digilent`` driver in libscopehal. This
driver connects using the ``twinlan`` transport to a `socket server <https://github.com/ngscopeclient/scopehal-waveforms-bridge>`_
which links against the Digilent WaveForms SDK. This provides network transparency, and allows the Digilent bridge
server to be packaged separately for distribution and only installed by users who require it.

As of 2022-03-09, analog input channels on the Analog Discovery Pro and Analog Discovery 2 have been tested and are
functional, however only basic edge triggering is implemented so far. Analog inputs on other devices likely work,
however only these two have been tested to date.

Analog outputs, digital inputs, and digital outputs are currently unimplemented, but are planned to be added in the
future.

digilent
~~~~~~~~

====================  ========  =========  =====
Device Family         Driver    Transport  Notes
====================  ========  =========  =====
Electronics Explorer  digilent  twinlan    Not tested, but probably works
Analog Discovery      digilent  twinlan    Not tested, but probably works
Analog Discovery 2    digilent  twinlan    No digital channel support \newline No analog output support
Analog Discovery Pro  digilent  twinlan    No digital channel support \newline No analog output support
Digital Discovery     digilent  twinlan    No digital channel support,\newline so pretty useless for now
====================  ========  =========  =====

Typical Performance (ADP3450, USB -> LAN)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ============  =====
Channels  Memory depth  WFM/s
========  ============  =====
4         64K           25.8
2         64K           32.3
1         64K           33.0
========  ============  =====

DreamSource Lab
---------------

DreamSourceLabs oscilloscopes and logic analyzers supported in their fork of sigrok (``libsigrok4DSL`` distributed as part of
their ``DSView`` software package) are supported through the ``dslabs`` driver in libscopehal. This driver connects using
the ``twinlan`` transport to a `socket server <https://github.com/ngscopeclient/scopehal-sigrok-bridge>`_ which links
against libsigrok4DSL. This provides network transparency, and allows the DSLabs bridge server to be packaged separately for
distribution and only installed by users who require it.

As of 2022-03-22, a DSCope U3P100 and a DSLogic U3Pro16 has been tested and works adequately. Other products may work
also, but are untested.

On DSCope: Only edge triggers are supported. "Any" edge is not supported. "Ch0 && Ch1" and "Ch0 || Ch1" trigger modes
are not supported.

On DSLogic: Only edge triggers are supported. All edges are supported. There is currently no way to configure a trigger on more
than one channel. Serial / multi-stage triggers are not supported.

Known issues pending fixes/refactoring:

*   Interleaved sample rates are not correctly reported in the timebase dialog (but are in the waveform display)
*   Trigger position is quantized to multiples of 1\% of total capture
*   Non-localhost performance, and responsiveness in general may suffer as a result of hacky flow control on waveform capture
*   DSLogic depth configuration is confusing and performance could be improved (currently only buffered more is supported)
*   DSLogic devices trigger even if pre-trigger buffer has not been filled, leading to a small pre-trigger waveform in some cases

dslabs
~~~~~~

================  ======  =========  =====
Device Family     Driver  Transport  Notes
================  ======  =========  =====
DScope U3P100     dslabs  twinlan    Tested, works
DSLogic U3P16     dslabs  twinlan    Tested, works
DSCope (others)   dslabs  twinlan    Not tested, but probably works
DSLogic (others)  dslabs  twinlan    Not tested, but probably works
================  ======  =========  =====

Typical DSCope Performance (DSCope U3P100, USB3, localhost)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ============  ===========  =====  ======================
Channels  Memory depth  Sample Rate  WFM/s  UI-unconstrained WFM/s
========  ============  ===========  =====  ======================
2         1M            100MS/s      14     50
2         5M            500MS/s      4.5    14
1         5M            1GS/s        8.3    32
========  ============  ===========  =====  ======================

Typical DSLogic Performance (DSLogic U3Pro16, USB3, localhost)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ============  ===========  =====  ======================
Channels  Memory depth  Sample Rate  WFM/s  UI-unconstrained WFM/s
========  ============  ===========  =====  ======================
16        500k          100MS/s      16     44
16        500k          500MS/s      16     55
========  ============  ===========  =====  ======================

EEVengers
---------

thunderscope
~~~~~~~~~~~~

This driver connects to the TS.NET application to control a ThunderScope.

It supports full-rate 1 Gsps streaming given suitably fast hardware.

====================  ============  =========  =====
Device Family         Driver        Transport  Notes
====================  ============  =========  =====
ThunderScope          thunderscope  twinlan    Use twinlan transport to TS.NET

====================  ============  =========  =====

Enjoy Digital
~~~~~~~~~~~~~

TODO (`scopehal:79 <https://github.com/ngscopeclient/scopehal/issues/79>`_)

Generic
-------

Drivers in this section are not specific to a particular manufacturer's products and support a wide variety of similar
devices.

socketcan
~~~~~~~~~

This driver exposes the Linux SocketCAN API as a stream of CAN messages which can be displayed as-is or used as input
to other filter graph blocks. When paired with the ``socketcan`` transport and a suitable CAN peripheral, it allows
ngscopeclient to be used as a CAN bus protocol analyzer. Since SocketCAN is a Linux-only API, this driver is not
available on other platforms.

Hantek
------

TODO (`scopehal:26 <https://github.com/ngscopeclient/scopehal/issues/26>`_)

Keysight
--------

Keysight devices support a similar similar SCPI command set across most device families. Many Keysight devices were
previously sold under the Agilent brand and use the same SCPI command set, so they are supported by the ``agilent``
driver.

Please see the table below for details of current hardware support:

agilent
~~~~~~~

====================  ========  =========  =====
Device Family         Driver    Transport  Notes
====================  ========  =========  =====
MSOX-2000 series      agilent
MSOX-3000 series      agilent
MSOX-3000T series     agilent
====================  ========  =========  =====

keysightdca
~~~~~~~~~~~

A driver for the Keysight/Agilent/HP DCA series of equivalent-time sampling oscilloscopes.

====================  ===========  =========  =====
Device Family         Driver       Transport  Notes
====================  ===========  =========  =====
86100A & keysightdca  keysightdca

====================  ===========  =========  =====

Pico Technologies
-----------------

Pico oscilloscopes all have slightly different command sets, but are supported using the ``pico`` driver in libscopehal.
This driver connects via a TCP socket to a socket server
`scopehal-pico-bridge <https://github.com/ngscopeclient/scopehal-pico-bridge>`_ which connects to the appropriate
instrument using Pico's binary SDK.

====================  ========  =========  =====
Device Family         Driver    Transport  Notes
====================  ========  =========  =====
3000D series          pico                 Early development, incomplete
6000E series          pico
====================  ========  =========  =====

pico
~~~~

Typical Performance (6824E, LAN)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ============  =====
Channels  Memory depth  WFM/s
========  ============  =====
8         1M            15.2
4         1M            30.5
2         1M            64.4
1         10M           12.2
1         50M           3.03
========  ============  =====

Rigol
-----

Rigol oscilloscopes have subtle differences in SCPI command set, but this is implemented with quirks handling in the
driver rather than needing different drivers for each scope family.

NOTE: DS1054Z firmware 00.04.02.SP4 is known to have problems with SCPI remote control
(`scopehal-apps:790 <https://github.com/ngscopeclient/scopehal-apps/issues/790>`_); it is unclear what other models and firmware versions may
be affected by this bug. If you encounter problems, please ensure your scope is running the latest firmware release
from Rigol before opening a support ticket.

====================  ========  =========  =====
Device Family         Driver    Transport  Notes
====================  ========  =========  =====
DS1100D/E             rigol
DS1000Z               rigol
MSO5000               rigol
DHO800                rigol
DHO900                rigol                no digital channels
DHO1000               rigol                untested
DHO4000               rigol                untested
====================  ========  =========  =====

rigol
~~~~~

Typical Performance (MSO5000 series, LAN)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ============  =====
Channels  Memory depth  WFM/s
========  ============  =====
4         10K           0.96
4         100K          0.91
4         1M            0.59
4         10M           0.13
1         100M          0.0601
4         25M           0.0568
2         50M           0.0568
========  ============  =====

Typical Performance (DHO800/900 series, LAN)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ============  =====  =====
Channels  Memory depth  WFM/s  Notes
========  ============  =====  =====
1         1K            11.9   live mode available for 1Kpt/single channel
2         1K            3.4
4         1K            1.66
1         10K           3.31
2         10K           2.90
4         10K           1.65
1         100K          3.30
4         100K          1.64
1         1M            1.63
4         1M            0.57
1         10M           0.30
4         10M           0.07
========  ============  =====  =====

Rohde & Schwarz
---------------

rs
~~

There is partial support for RTM3000 (and possibly others, untested) however it appears to have bitrotted.

TODO (`scopehal:59 <https://github.com/ngscopeclient/scopehal/issues/59>`_)

rs_rto6
~~~~~~~

This driver supports the newer RTO6 family scopes (and possibly others, untested).

Saleae
------

TODO (`scopehal:16 <https://github.com/ngscopeclient/scopehal/issues/16>`_)

Siglent
-------

A driver for SDS2000X+/HD is available in the codebase which has been developed according to Siglent offical documentation
(Programming Guide PG01-E11A). This driver should be functional across the 'next generation' SDS800X HD, SDS1000X HD, SDS2000X+,
SDS2000X HD, SDS5000X, SDS6000A/L/Pro and SDS7000A scopes. It has been primarily developed using the SDS2000X^ and SDS2000X HD.
Some older generation scopes are supported as well.

Digital channels are not supported on any scope yet, due to lack of an MSO probe to test with. Many trigger types are
not yet supported.

=====================  =======  =========  =====
Device Family          Driver   Transport  Notes
=====================  =======  =========  =====
SDS1000X-E series      siglent  lan        Initialises, triggers and downloads waveforms. More testing needed
SDS2000X-E series      siglent  lan        Initialises, triggers and downloads waveforms. More testing needed
SDS800X HD series      siglent  lan        Basic functionality complete/tested.
SDS1000X HD series     siglent  lan        Basic functionality complete, needs testing.
SDS2000X+ series       siglent  lan        Basic functionality complete.
SDS2000X HD series     siglent  lan        Tested and works well on SDS2354x HD.
SDS3000X HD series     siglent  lan        Basic functionality complete, needs testing.
SDS5000X series        siglent  lan        Initialises, triggers and downloads waveforms. More testing needed
SDS6000A/L/Pro series  siglent  lan        Tested and works well on SDS6204A. 10/12 bit models NOT supported, but unavailable for dev (not sold in western markets).
SDS7000A series        siglent  lan        Basic functionality complete, needs testing.
=====================  =======  =========  =====

siglent
~~~~~~~

Typical Performance (SDS2104X^, LAN)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _siglent_sample:
.. figure:: images/siglent-samples.png

    Siglent sample speed for various combinations of depth and channels


========  ============  =====
Channels  Memory depth  WFM/s
========  ============  =====
1         5-100K        2.3
2         5-100K        1.6
3         5-100K        1.2
4         5-100K        1
1         10M           0.5
2-4       10M           0.15
========  ============  =====

These figures were obtained from a SDS2104X^ running firmware version 1.3.7R5. Different scopes and software
revisions may vary.

Typical Performance (SDS2104X HD, LAN)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ============  =====
Channels  Memory depth  WFM/s
========  ============  =====
1         10K           8.2
2         10K           7.7
4         10K           5.4
1         100K          7.1
4         100K          4.2
1         5M            0.72
4         5M            0.09
========  ============  =====

These figures were obtained from a SDS2104X HD running firmware version 1.2.2.9.

Teledyne LeCroy / LeCroy
------------------------

Teledyne LeCroy (and older LeCroy) devices use the same driver, but two different transports for LAN connections.

While all Teledyne LeCroy / LeCroy devices use almost identical SCPI command sets, Windows based devices running
XStream or MAUI use a custom framing protocol (``vicp``) around the SCPI data while the lower end RTOS based devices use
raw SCPI over TCP (``lan``).

Please see the table below for details on which configuration to use with  your hardware.

=============  ======  =========  =====
Device Family  Driver  Transport  Notes
=============  ======  =========  =====
DDA            lecroy  vicp       Tested on DDA5000A series
HDO            lecroy  vicp       Tested on HDO9000 series
LabMaster      lecroy  vicp       Untested, but should work for 4-channel setups
MDA            lecroy  vicp       Untested, but should work
SDA            lecroy  vicp       Tested on SDA 8Zi and 8Zi-A series
T3DSO          ???     ???        Untested
WaveAce        ???     ???        Untested
WaveJet        ???     ???        Untested
WaveMaster     lecroy  vicp       Same hardware as SDA/DDA
WaveRunner     lecroy  vicp       Tested on WaveRunner Xi, 8000, and 9000 series
WaveSurfer     lecroy  vicp       Tested on WaveSurfer 3000 series
=============  ======  =========  =====

lecroy
~~~~~~

This is the primary driver for MAUI based Teledyne LeCroy / LeCroy devices.

This driver has been tested on a wide range of Teledyne LeCroy / LeCroy hardware. It should be compatible with any
Teledyne LeCroy or LeCroy oscilloscope running Windows XP or newer and the MAUI or XStream software.

Typical Performance (HDO9204, VICP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ============  =====
Channels  Memory depth  WFM/s
========  ============  =====
1         100K          >50
1         400K          29 - 35
2         100K          30 - 40
4         100K          17 - 21
1         2M            9 - 11
1         10M           2.2 - 2.6
4         1M            5.2 - 6.5
1         64M           0.41 - 0.42
2         64M           0.21 - 0.23
4         64M           0.12 - 0.13
========  ============  =====

Typical Performance (WaveRunner 8404M-MS, VICP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ============  =====
Channels  Memory depth  WFM/s
========  ============  =====
1         80K           35 - 45
2         80K           35 - 45
2         800K          16 - 17
2         8M            3.1 - 3.2
========  ============  =====

lecroy_fwp
~~~~~~~~~~

This is a special performance-enhanced extension of the base ``lecroy`` driver which takes advantage of the FastWavePort
feature of the instrument to gain high speed access to waveform data via shared memory. Waveforms are pulled from
shared memory when a synchronization event fires, then pushed to the client via a separate TCP socket on port 1862.

On low latency LANs, typical performance increases observed with SDA 8Zi series instruments are on the order of 2x
throughput vs using the base driver downloading waveforms via SCPI. On higher latency connections such as VPNs, the
performance increase is likely to be even higher because the push-based model eliminates the need for polling (which
performs increasingly poorly as latency increases).

To use this driver, your instrument must have the XDEV software option installed and the
`scopehal-fwp-bridge <https://github.com/ngscopeclient/scopehal-fwp-bridge>`_ server application running. If the
bridge or option are not detected, the driver falls back to SCPI waveform download and will behave identically to the
base ``lecroy`` driver.

There are some limitations to be aware of with this driver:

*   Maxmimum memory depth is limited to no more than 40M samples per channel, regardless of installed instrument
    memory. This is an architectural limitation of the FastWavePort API; the next generation FastMultiWavePort API eliminates
    this restriction however scopehal-fwp-bridge does not yet support it due to poor documentation.

*   MSO channels are not supported, because neither FastWavePort nor FastMultiWavePort provide shared memory access to
    digital channel data. There is no known workaround for this given current instrument APIs.

*   A maximum of four analog channels are supported even if the instrument actually has eight. There are no major
    technical blockers to fixing this under FastWavePort however no 8-channel instruments are available to the developers as
    of this writing, so there is no way to test potential fixes. FastMultiWavePort has a limit of four channels per instance,
    but it may be possible to instantiate multiple copies of the FastMultiWavePort block to work around this.

*   Math functions F9-F12 are used by the FastWavePort blocks and cannot be used for other math functions.

Tektronix
---------

This driver is being primarily developed on a MSO64. It supports SCPI over LXI VXI-11 or TCP sockets.

The hardware supports USBTMC, however waveform download via USBTMC does not work with libscopehal for unknown reasons.

=============  =========  =========  =====
Device Family  Driver     Transport  Notes
=============  =========  =========  =====
MSO5 series    tektronix  lan, lxi
MSO6 series    tektronix  lan, lxi
=============  =========  =========  =====

Note regarding ``lan`` transport on MSO5/6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default settings for raw SCPI access on the MSO6 series use a full terminal emulator rather than raw SCPI
commands. To remove the prompts and help text, go to ``Utility | I/O``, then under the Socket Server panel select protocol
``None`` rather than the default of ``Terminal``.

Typical Performance (MSO64, LXI, embedded OS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========  ============  =====
Channels  Memory depth  WFM/s
========  ============  =====
1         50K           10.3 - 11.4
2         50K           6.7 - 7.2
4         50K           5.1 - 5.3
1         500K          8.7 - 9.5
4         500K          3.8 - 3.9
========  ============  =====

tinySA
------

This driver is meant to be used with tinySA and tinySA ULTRA spectrum analyzers.

It has been developed and tested on a tinySA ULTRA.

The communication with the device is made with UART transport layer.

=============  ========  =========  =====
Device Family  Driver    Transport  Notes
=============  ========  =========  =====
tinySA         tiny_sa   uart       Not tested but should work
tinySA ULTRA   tiny_sa   uart       Driver tested on this device
=============  ========  =========  =====

Xilinx
------

TODO (`scopehal:40 <https://github.com/ngscopeclient/scopehal/issues/40>`_)
