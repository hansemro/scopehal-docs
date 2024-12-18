Getting Started
===============

Host System Requirements
------------------------

The majority of development is performed on Linux operating systems (primarily Debian) so this is the most well
tested platform, however Windows and Mac OS are also supported.

Any 64-bit Intel or AMD processor, or Apple Silicon Mac, should be able to run ngscopeclient. If AVX2 and/or AVX512F
support is present ngscopeclient will use special optimized versions of some signal processing functions, however
neither instruction set is required. Other (non Apple Silicon) ARM64 platforms may work if a compatible GPU is
available, but have not been tested. We don't actively test on 32-bit platforms due to the significant RAM
requirements, but we won't stop you from trying and would love to hear if you get it working.

A mouse with scroll wheel, or touchpad with scroll gesture support, is mandatory to enable full use of the UI. We may
explore alternative input methods for some UI elements in the future.

Any GPU with Vulkan support should be able to run ngscopeclient, however Vulkan 1.2 will deliver better performance.
The minimum supported GPUs are:

* NVIDIA: Maxwell architecture (GeForce GTX 700 series and newer, February 2014)
* AMD: GCN based (Radeon HD 7000 and newer, January 2012)
* Intel: Iris Plus 540 or HD Graphics 520 (Skylake, August 2015)
* Apple: all Apple Silicon devices (M1 and newer). Newer Intel devices with Metal support should work but have not
  been tested.

Note that many virtual machine graphics stacks (e.g. VMWare) do not provide Vulkan unless a PCIe passthrough GPU is
being used.

The minimum RAM requirement to launch ngscopeclient is relatively small; however, actual memory consumption is
heavily dependent on workload and can easily reach into the tens of gigabytes when doing complex analysis on many
channels with deep history.

Typical RAM consumption examples:

* Default configuration with demo scope (4 channels 100K points, 10 waveforms of history, no analysis): 250 MB
* 4M point live streaming with 10 waveforms of history, eye pattern, 8B/10B decode, and jitter histogram: 650 MB
* Single 512M point waveform, no analysis or history: 2.1 GB
* 512M point P/N channel waveforms with CDR and eye pattern, no history: 8.3 GB

Large amounts of GPU RAM are required for working with deep waveforms, especially if you intend to perform
complex analysis on them. Analog waveforms are stored in 32-bit floating point format internally, so a single 256
megapoint waveform will consume 1GB of GPU memory. Intermediate results in multi-step filter pipelines require GPU
memory as well, even if not displayed.

The maximum supported waveform size depends on your Vulkan implementation but is typically :math:`2~32` bytes (4 GB).
This translates to one gigapoint analog or four gigapoints digital.

Instrument Support
------------------

ngscopeclient uses the libscopehal library to communicate with instruments, so any libscopehal-compatible hardware
should work with ngscopeclient. See the :ref:`Oscilloscope Drivers <sec:scope-drivers>` section for more details on
which hardware is supported and how to configure specific drivers.

Installation
------------

Official Releases
~~~~~~~~~~~~~~~~~

Prebuilt binary packages are available for some of our supported platforms.

The latest released binaries can be downloaded from GitHub at (FIXME url here).

Development Builds
~~~~~~~~~~~~~~~~~~

If you are feeling adventurous and want to try bleeding-edge code, or are testing a fix at a developer's request,
packages for a limited set of platforms (currently Ubuntu 20.04, 22.04, 24.04, and Windows) are automatically built
each commit as part of the GitHub CI pipeline.

To access development packages, log into GitHub (sorry, development binaries are not available to
anonymous users - this is on GitHub's end and not under our control) and go to
https://github.com/ngscopeclient/scopehal-apps/actions. Select build-ubuntu or build-windows as appropriate,
click the commit you wish to test, and download the appropriate .msi or .deb package.

Compilation
-----------

ngscopeclient can be compiled on Linux, macOS, and Windows. While the compilation process is generally similar, various
steps differ among platform and distro.

TODO: update steps for building (sphinx) HTML+PDF documentation.

Linux
~~~~~

1.  Install dependencies:

    .. tabs::

        .. tab:: **Debian**

            Basic requirements:

            .. code-block:: sh

                sudo apt-get install build-essential git cmake pkgconf \
                    libgtkmm-3.0-dev libcairomm-1.0-dev libsigc++-2.0-dev \
                    libyaml-cpp-dev catch2 libglfw3-dev curl xzip \
                    libhidapi-dev

            On Debian bookworm and later, you can use system-provided Vulkan packages. Skip this on Debian bullseye, or if you
            choose to use the Vulkan SDK instead:

            .. code-block:: sh

                sudo apt-get install libvulkan-dev glslang-dev \
                    glslang-tools spirv-tools glslc

            On Debian bullseye, you will need cmake from backports:

            .. code-block:: sh

                sudo bash -c 'echo "deb http://deb.debian.org/debian bullseye-backports main" >> \
                    /etc/apt/sources.list.d/bullseye-backports.list'
                sudo apt-get update
                sudo apt-get install cmake/bullseye-backports

            To build the LXI component (needed if you have LXI- or VXI-11-based instruments):

            .. code-block:: sh

                sudo apt install liblxi-dev libtirpc-dev

            For GPIB, you will need to install Linux-GPIB; instructions for this are out of scope here.

            To build the documentation, you will also need LaTeX packages:

            .. code-block:: sh

                sudo apt install texlive texlive-fonts-extra \
                    texlive-extra-utils

        .. tab:: **Ubuntu**

            Basic requirements:

            .. code-block:: sh

                sudo apt install build-essential git cmake pkgconf \
                    libgtkmm-3.0-dev libcairomm-1.0-dev \
                    libsigc++-2.0-dev libyaml-cpp-dev catch2 \
                    libglfw3-dev curl xzip libhidapi-dev

            On Ubuntu 22.10 and earlier (including 20.04 and 22.04), you will need to use the Vulkan SDK.
            Instructions for installing this are in a later step. On Ubuntu 23.04 and later, you can instead
            use system-provided Vulkan packages:

            .. code-block:: sh

                sudo apt-get install libvulkan-dev glslang-dev \
                    glslang-tools spirv-tools glslc


            To build the LXI component (needed if you have LXI- or VXI-11-based instruments):

            .. code-block:: sh

                sudo apt install liblxi-dev libtirpc-dev

            For GPIB, you will need to install Linux-GPIB; instructions for this are out of scope here.

            To build the documentation, you will also need LaTeX packages:

            .. code-block:: sh

                sudo apt install texlive texlive-fonts-extra \
                    texlive-extra-utils


        .. tab:: **Fedora**

            Basic requirements:

            .. code-block:: sh

                sudo dnf install git gcc g++ cmake make pkgconf \
                    cairomm-devel gtk3-devel libsigc++30-devel \
                    yaml-cpp-devel catch-devel glfw-devel \
                    libhidapi-dev

            System-provided Vulkan packages. Skip these if you choose to use the Vulkan SDK instead:

            .. code-block:: sh

                sudo dnf install vulkan-headers vulkan-loader-devel \
                    glslang-devel  glslc libshaderc-devel \
                    spirv-tools-devel

            To build the LXI component (needed if you have LXI- or VXI-11-based instruments):

            .. code-block:: sh

                sudo dnf install liblxi-devel libtirpc-devel

            For GPIB, you will need to install Linux-GPIB; instructions for this are out of scope here.

            To build the documentation, you will also need LaTeX packages:

            .. code-block:: sh

                sudo dnf install texlive

        .. tab:: **Alpine Linux**

            As Alpine Linux uses musl libc, you will need to use system-provided Vulkan packages, and not the Vulkan SDK.

            .. code-block:: sh

                apk add git gcc g++ cmake make pkgconf cairomm-dev \
                    gtk+3.0-dev libsigc++-dev yaml-cpp-dev catch2-3 \
                    vulkan-loader-dev glslang-dev glslang-static \
                    glfw-dev shaderc-dev spirv-tools-dev libhidapi-dev

    If you are using an older stable release (such as CentOS 7), you may need to install some dependencies from source.

2.  Install Vulkan SDK:

    In many cases, you can install the SDK components from distro-provided repositories, which is covered above. When
    possible, this is preferred over installing the Vulkan SDK. If you choose not to, or are running a Linux distro that
    does not provide these packages (for instance, Debian Bullseye, Ubuntu versions prior to 23.04, or other stable
    distros), the following instructions cover installing and loading the Vulkan SDK.

    The latest tested SDK at the time of documentation update is version 1.3.275.0. Newer SDKs are supported, but breaking
    changes sometimes take place.
    If you are using a newer SDK and run into problems, please file a bug report.

    If you are using Ubuntu 20.04 or 22.04, you may install the
    `.deb packaged SDK release <https://packages.lunarg.com>` instead of following the instructions below. This may
    work for Debian as well but is not supported.

    Alternatively, to use the tarball packaged SDK, download and unpack the tarball.
    `You can manually download the SDK <https://vulkan.lunarg.com/sdk/home>`, or do the following:

    .. code-block:: sh

        cd ~
        mkdir VulkanSDK
        cd VulkanSDK
        curl -LO 'https://vulkan.lunarg.com/sdk/download/1.3.275.0/linux/vulkansdk-linux-x86_64-1.3.275.0.tar.xz'
        tar xfv vulkansdk-linux-x86_64-1.3.275.0.tar.xz

    And then source the `setup-env.sh` file:

    .. code-block:: sh

        source "$HOME/VulkanSDK/1.3.275.0/setup-env.sh"

    When using the tarball-packaged SDK, you will need to source the `setup-env.sh` file any time you want to compile
    or run ngscopeclient. For convenience, you can add this to your `.bash\_profile` or equivalent:

    .. code-block:: sh

        echo "source \"$HOME/VulkanSDK/1.3.275.0/setup-env.sh\"" >> ~/.bash_profile

3.  Build scopehal and scopehal-apps:

    .. code-block:: sh

        cd ~
        git clone --recursive https://github.com/ngscopeclient/scopehal-apps.git
        cd scopehal-apps
        mkdir build
        cd build
        cmake .. -DCMAKE_BUILD_TYPE=Release
        make -j4

macOS
~~~~~

1. Install dependencies:

    You will need Xcode (either from the App Store or the Apple developer site); after installing, run it once for it
    to install system components. This provides gcc, g++, make, and similar required packages.

    With Homebrew (`brew.sh <https://brew.sh>`):

    Basic requirements:

    .. code-block:: sh

        brew install pkg-config cairomm libsigc++ glfw cmake yaml-cpp glew catch2 libomp hidapi

2. Install Vulkan SDK components (skip if using the Vulkan SDK):

    .. code-block:: sh

        brew install vulkan-headers vulkan-loader glslang shaderc spirv-tools molten-vk

    Alternatively, install the Vulkan SDK:

    `Download and install the Vulkan SDK. <https://vulkan.lunarg.com/sdk/home}{Download and install the Vulkan SDK>`.
    The latest tested SDK at the time of documentation update is version 1.3.275.0. Newer SDKs are supported, but breaking
    changes sometimes take place.
    If you are using a newer SDK and run into problems, please file a bug report.

    And then source the `setup-env.sh` file:

    .. code-block:: sh

        source "$HOME/VulkanSDK/1.3.275.0/setup-env.sh"

    When using the SDK, you will need to source the `setup-env.sh` file any time you want to compile or run ngscopeclient.
    For convenience, you can add this to your `.zprofile` or equivalent:

    .. code-block:: sh

        echo "source \"$HOME/VulkanSDK/1.3.275.0/setup-env.sh\"" >> ~/.zprofile

3.  Build scopehal and scopehal-apps:

    .. code-block:: sh

        cd ~
        git clone --recursive https://github.com/ngscopeclient/scopehal-apps.git
        cd scopehal-apps
        mkdir build
        cd build
        cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH="$(brew --prefix);$(brew --prefix)/opt/libomp"
        make -j4

Windows
~~~~~~~

On Windows, we make use of the MSYS2 development environment, which gives us access to the MingGW-w64 toolchain.
Since this toolchain allows ngscopeclient to be compiled as a native Windows application, the project might be run
outside of MSYS2.

Building from source
^^^^^^^^^^^^^^^^^^^^

All following steps are to be done in a UCRT64 shell.

1.  Download and install MSYS2. You can download it from `msys2.org <https://www.msys2.org/>`_ or
    `github.com/msys2/msys2-installer/releases <https://github.com/msys2/msys2-installer/releases>`_


    The following steps can be done in any MSYS-provided shell.

2.  Install git and the toolchain:

    .. code-block:: sh

        pacman -S git wget mingw-w64-ucrt-x86_64-cmake \
            mingw-w64-ucrt-x86_64-toolchain

3.  Install general dependencies:

    .. code-block:: sh

        pacman -S mingw-w64-ucrt-x86_64-libsigc++ \
            mingw-w64-ucrt-x86_64-cairomm \
            mingw-w64-ucrt-x86_64-yaml-cpp \
            mingw-w64-ucrt-x86_64-glfw \
            mingw-w64-ucrt-x86_64-catch \
            mingw-w64-ucrt-x86_64-hidapi

4.  Install Vulkan dependencies:

    .. code-block:: sh

        pacman -S mingw-w64-ucrt-x86_64-vulkan-headers \
            mingw-w64-ucrt-x86_64-vulkan-loader \
            mingw-w64-ucrt-x86_64-shaderc \
            mingw-w64-ucrt-x86_64-glslang \
            mingw-w64-ucrt-x86_64-spirv-tools

5.  Install FFTS:

    .. code-block:: sh

        pacman -S mingw-w64-ucrt-x86_64-ffts


6.  Check out the code

    .. code-block:: sh

        cd ~
        git clone --recursive https://github.com/ngscopeclient/scopehal-apps

7.  Build manually inside a UCRT64 shell:

    .. code-block:: sh

        cd scopehal-apps
        mkdir build
        cd build
        cmake ..
        ninja -j4

8.  Optional, to build MSI installer:

    `Download and install WiX Toolset <https://github.com/wixtoolset/wix3/releases>`.

    If you install it to the path ``C:\textbackslash Program Files (x86)\textbackslash WiX Toolset v3.14``
    run the following cmake command instead of ``cmake ..`` mentioned earlier:

    .. code-block:: sh

        cmake .. -DWIXPATH="C:\Program Files (x86)\WiX Toolset v3.14\bin"

    ``ninja`` compilation will now generate the installer after binaries.

9.  Install scopehal and scopehal-apps:

    At the moment, installation scripts are not yet complete.
    The binaries can be found in the build directory, such as ngscopeclient in ``$HOME/scopehal-apps/build/src/ngscopeclient``.

    FIXME: document how to build the MSI or do system-wide install

Running ngscopeclient
---------------------

When running ngscopeclient with no arguments, an empty session (:numref:`empty-window`) is created. To perform useful
work, you can:

* Open a saved session and reconnect to the instruments (``File | Open Online``)
* Open a saved session without reconnecting to the instruments (``File | Open Offline``)
* Open a recently used session (``File | Recent Files``)
* Import waveforms from a third party file format(``Add | Import``)
* Connect to an instrument (``Add | Oscilloscope``, ``Add | Multimeter``, etc.)
* Generate a synthetic waveform (``Add | Generate``)

.. _empty-window:
.. figure:: ng-images/empty-window.png
    :figclass: align-center

    Empty ngscopeclient session

Console verbosity arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

ngscopeclient takes standard liblogtools arguments for controlling console debug verbosity.

If no verbosity level is specified, the default is "notice" (3). (We suggest using ``--debug`` for routine use
until the v1.0 release to aid in troubleshooting.)

* ``--debug``

  Sets the verbosity level to ``debug`` (5).

* ``-l [file]``, ``--logfile [file]``

  Writes a copy of all log messages to ``file``. This is preferred over simply redirecting output with pipes, as
  console escape sequences are stripped from the file log output.

* ``-L [file]``, ``--logfile-lines [file]``

  Same as ``--logfile`` except line buffering is turned on.

* ``-q``, ``--quiet``

  Reduces the verbosity level by one. Can be specified more than once to lower verbosity by several steps.

* ``--trace [class]``, ``--trace [class::function]``

  Enables extra debug output from the class ``class`` or the function ``class::function``. Has no effect unless
  ``--debug`` is also specified.

* ``--stdout-only``

  Sends all logging output to stdout. By default, error (level 1) and warning (level 2) messages go to stderr.

* ``--verbose``

  Sets the verbosity level to "verbose" (4).
