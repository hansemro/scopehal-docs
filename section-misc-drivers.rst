.. _sec:misc-drivers:

Miscellaneous Drivers
=====================

This chapter describes all of the available drivers for miscellaneous instruments which do not fit in any other
category.

Generic
-------

=============  =========  =========  =====
Device Family  Driver     Transport  Notes
=============  =========  =========  =====
N/A            csvstream  Any

=============  =========  =========  =====

csvstream
~~~~~~~~~

This driver exposes the most recent line from a stream of comma-separated value (CSV) data as a series of analog scalar
channels.

It is primarily intended for extracting low rate I2C sensor readings and ADC values from an embedded DUT, so that that
these values may be plotted alongside multimeter/power supply readings or other data coming from more conventional
instrumentation.

The data may come from any supported transport, however it is expected that the most likely scenario is either direct
connection to a local serial port (``uart`` transport), or a TCP socket connected to either a remote UART using socat or
an embedded TCP server (``lan`` transport).

Data must be generally line oriented and UTF-8 or 7-bit ASCII encoded.

In order to enable csvstream data to share a UART also used by other traffic such as a debug console or syslog, all
lines must contain one of three magic prefixes as shown below. Any content in the line before the prefix (such as a
timestamp) is ignored.

Upon initial connection, the driver will have a single channel called ``CH1``. At any time, if the number of fields in a
received CSV line exceeds the current channel count, a new channel will be created. If a partial line is received, the
values in the missing columns are unchanged but the channel will not be deleted.

*   **CSV-NAME**: Contains channel name data.

    Example: CSV-NAME,Temperature,3V3,RxLevel

*   **CSV-UNIT**: Contains channel unit data (using the text encodings used by the libscopehal Unit class).

    Example: CSV-UNIT,°C,V,dBm

*   **CSV-DATA**: Contains channel value data.

    Example: CSV-DATA,31.41,3.291,-59.1
