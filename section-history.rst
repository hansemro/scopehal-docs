.. _sec:history:

History
=======

ngscopeclient saves a rolling buffer of previous waveforms in memory, allowing you to go back in time and see previous
state of the system being debugged. Clicking on a timestamp in the history view (:numref:`historyview`) pauses
acquisition and loads the historical waveform data for analysis. History is captured regardless of whether the window
is visible or not.

.. _historyview:
.. figure:: ng-images/history.png
    :figclass: align-center

    Waveform history view

The history depth defaults to 10 waveforms, but can be set arbitrarily within the limits of available RAM. Older
waveforms beyond the history limit are deleted as new waveforms are acquired. Any single waveform in history may also
be deleted by right clicking on the line and selecting ``delete`` from the menu.

Pinning
-------

Interesting waveforms may be "pinned" in the history by checking the box in the ``pin`` column of the history view.
Pinned waveforms are guaranteed to remain in the history buffer even when new waveforms arrive; only unpinned waveforms
are eligible for automatic deletion to make space for incoming data.

If a waveform contains markers (:ref:`sec:markers`), it is automatically pinned and cannot be unpinned unless the
marker (or entire waveform) is deleted. This prevents accidental loss of an important waveform: if the event was
important enough to mark and name, it is probably worth keeping around.

Labeling
--------

Arbitrary text names may be assigned to a waveform by clicking the corresponding cell in the ``label`` column.
Waveforms with a label are automatically pinned, since assigning a label implies the waveform is important.

Estimating Waveform Memory Usage
--------------------------------

When selecting a maximum depth for the history, it is important to pick a reasonable limit to avoid running out of RAM!
ngscopeclient will happily fill tens or hundreds of gigabytes of memory with deep waveforms if given a chance. Memory
usage of waveform data can be roughly estimated as 16 + sizeof(sample type) bytes per point, since each sample contains a
64-bit timestamp and duration plus the sample data.

For example, an analog sample takes 20 bytes of RAM (16 of time plus a 32-bit floating point voltage measurement) per
sample. Thus, a 1M point analog waveform takes approximately 20 MB of RAM per channel, or 80 MB per capture on a
four-channel oscilloscope with all channels enabled.

On the larger side, a 10M point four channel capture would use 800 MB and a 64M point deep-memory capture would use 5
GB. A deep history setting, such as 100 waveforms, is thus wildly inappropriate for such deep captures! A future
software release may support spilling waveform data to a temporary directory on disk, permitting effectively unlimited
history depth given sufficient disk space.

Digital waveforms use one byte per sample for the actual measurement, so 17 MB per channel for a 1M point waveform.
Most logic analyzer or MSO drivers for libscopehal will perform automatic de-duplication when a waveform goes several
clock cycles with no toggles, so the actual memory usage is likely to be significantly less than this.

Filter memory usage varies depending on the specific filter in question, however it is typically not a large
contributor to the overall ngscopeclient RAM footprint when using history mode because filters are evaluated
dynamically each time a waveform is pulled from history rather than having output cached for every historical waveform.
Thus, at most one copy of each filter's output is present in memory regardless of history depth.
