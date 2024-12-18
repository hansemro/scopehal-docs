.. _sec:rfgen-drivers:

RF Generator Drivers
====================

This chapter describes all of the available drivers for RF synthesizers, vector signal generators, and similar devices.

Siglent
-------

=============  ===========  =========  =====
Device Family  Driver       Transport  Notes
=============  ===========  =========  =====
SSG3000X       Unknown      Unknown    May be compatible with the siglent_ssg driver, but not tested
SSG5000A       Unknown      Unknown    May be compatible with the siglent_ssg driver, but not tested
SSG5000X       siglent_ssg  lan        Only tested via lan transport, but USBTMC and serial are available too
=============  ===========  =========  =====

siglent_ssg
~~~~~~~~~~~

This driver was developed on a SSG5060X-V and should support the other models in the SSG5000X family (SSG5040X,
SSG5060X, and SSG5040X-V). It is unknown whether it will function at all with the SSG3000X or 5000A families in its
current state; additional development will likely be needed for full support.
