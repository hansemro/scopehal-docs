.. _sec:transports:

Transports
==========

Libscopehal uses a ``transport`` object in order to pass commands and data to instruments, in order to decouple the
specifics of LXI, USBTMC, etc. from individual instrument drivers. This section describes the supported transports and
their usage and limitations.

Not all transports are possible to use with any given driver due to hardware limitations or software/firmware quirks.
For details on which transport(s) are usable with a particular instrument, consult the documentation for that device's
driver.

.. WARNING::
   Currently, ngscopeclient does not yet support instrument arguments from the command line. Arguments shall be specified
   under ``Path`` in the connection dialog (:numref:`basic-connect`).

gpib
----

SCPI over GPIB.

This transport takes up to four arguments: GPIB board index, primary address, secondary address, and timeout value.
Only board index and primary address are required. We currently support using a single GPIB device per GPIB board
(interface) in a ngscopeclient session. You cannot currently access multiple devices in the same or across instances.
Better support for multiple instrument on a single board is planned.

.. NOTE::
    The current implementation of this driver only works on Linux, using the linux-gpib library.

Example:

.. code-block::

    ngscopeclient myscope:keysightdca:gpib:0:7

lan
---

SCPI over TCP with no further encapsulation.

This transport takes two arguments: hostname/IP and port number.

If port number is not specified, uses TCP port 5025 (IANA assigned) by default. Note that Rigol oscilloscopes use the
non-standard port 5555, not 5025, so the port number must always be specified when using a Rigol instrument.

Example:

.. code-block::

    ngscopeclient myscope:rigol:lan:192.0.2.9:5555

lxi
---

SCPI over LXI VXI-11.

Note that due to the remote procedure call paradigm used by LXI, it is not possible to batch multiple outstanding
requests to an instrument when using this transport. Some instruments may experience reduced performance when using LXI
as the transport. Drivers which require command batching may not be able to use LXI VXI-11 as the transport even if the
instrument supports it.

Example:

.. code-block::

    ngscopeclient myscope:tektronix:lxi:192.0.2.9

null
----

This transport does nothing, and is used as a placeholder for development simulations or non-SCPI instruments.

NOTE: Due to limitations of the current command line argument parsing code, an argument must be provided to all
transports, including this one, when connecting via the command line. Since the argument is ignored, any non-empty
string may be used.

Example:

.. code-block::

    ngscopeclient sim:demo:null:blah

socketcan
---------

This transport provides a bridge for accessing the native Linux SocketCAN API from the scopehal driver layer. When
paired with the ``socketcan`` oscilloscope driver and a suitable CAN peripheral, it allows ngscopeclient to be used as a
CAN bus protocol analyzer. Since SocketCAN is a Linux-only API, this transport is not available on other platforms.

This transport takes one argument: the device name (e.g. ``can0``)

twinlan
-------

This transport is used by some Antikernel Labs oscilloscopes, as well as most of the bridge servers used for interfacing
libscopehal with USB oscilloscopes' SDKs. It takes three arguments: hostname/IP and two port numbers.

It uses two TCP sockets on different ports. The first carries SCPI text (as in the ``lan`` transport), and the second is
for binary waveform data.

If port numbers are not specified, the SCPI port defaults to the IANA standard of 5025, and the data port defaults to
5026. If the SCPI port but not the data port is specified, the data port defaults to the SCPI port plus one.

uart
----

SCPI over RS-232 or USB-UART.

This transport takes 3 arguments: device path (required), baud rate (optional), and flags (optional). If baud rate is not specified, it
defaults to 115200.

Example:

.. code-block::

    ngscopeclient myscope:rigol:uart:/dev/ttyUSB0:115200

Some devices, like the NanoVNA, need to activate the DTR line to communicate. This can be achieved by adding the DTR flag to the connection string.

Example:

.. code-block::

    ngscopeclient NanoVNA-F:nanovna:uart:COM6:115200:DTR

usbtmc
------

SCPI over USB Test & Measurement Class protocol.

This transport takes two arguments: the path to the usbtmc kernel device object and the TMC transfer size (optional).
As Workaround for Siglent SDS1x04x-E set size to 48.

NOTE: The current implementation of this driver only works on Linux. There is currently no support for USBTMC on
Windows (`scopehal:301 <https://github.com/ngscopeclient/scopehal/issues/301>`_)

Example:

.. code-block::

    ngscopeclient myscope:siglent:usbtmc:/dev/usbtmc0:48

vicp
----

SCPI over Teledyne LeCroy Virtual Instrument Control Protocol.

This transport takes two arguments: hostname/IP and port number.

If port number is not specified, uses TCP port 1861 (IANA assigned) by default.

Example:

.. code-block::

    ngscopeclient myscope:lecroy:vicp:192.0.2.9

hid
---

This transport layer is usually used by binary drivers to communicate with Test & Measurement equiment over USB.

This transport takes two arguments: vendor ID (hex) and product ID (hex).

Optionally a third argument can be added with the instrument's serial number.
If not provided, the instrument's serial number is automatically pulled at first connection and stored in the connection string.

Example:

.. code-block::

    ngscopeclient AlientekDP100:alientek_dp:hid:2e3c:af01
