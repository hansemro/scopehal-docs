.. _sec:bert-drivers:

BERT Drivers
============

This chapter describes all of the available drivers for bit error rate testers (BERTs)

Antikernel Labs
---------------

=============  ============  =========  =====
Device Family  Driver        Transport  Notes
=============  ============  =========  =====
AKL-TXB1       akl.crossbar  lan

=============  ============  =========  =====

akl.crossbar
~~~~~~~~~~~~

This is the driver for the `AKL-TXB1 <https://github.com/azonenberg/triggercrossbar>`_ trigger crossbar and CDR
trigger system. The front panel transceiver ports can also be used as a BERT.

MultiLANE
---------

=============  ============  =========  =====
Device Family  Driver        Transport  Notes
=============  ============  =========  =====
ML4039-BTP     mlbert        lan        Use `scopehal-mlbert-bridge <https://github.com/ngscopeclient/scopehal-mlbert-bridge>`_

=============  ============  =========  =====

mlbert
~~~~~~

This driver is intended to connect via the
`scopehal-mlbert-bridge <https://github.com/ngscopeclient/scopehal-mlbert-bridge>`_ server for network transparency
and does not directly link to the MultiLANE SDK or talk directly to the instrument. The bridge requires a Windows PC
since MultiLANE's SDK is Windows only, however the libscopehal clientside driver can run on any supported OS.

It was developed using a ML4039-BTP but may work with other similar models as well.
