# optimuspy

Python Launcher with Optimus Enablement

## Problem & Solution

I am using python for developing 3D applications and games. I have a dedicated GPU and an Intel HD Graphics 630. My applications run with the Intel HD Graphics 630 unless changed in the nVidia control panel.

I started googling then I found a solution how to programatically enable the dedicated graphics card. This problem only occurres on Optimus Systems. The solution is simple. An integer variable called _NvOptimusEnablement_ should be exported in order to enable the nVidia card.

Unfortunately exporting this variable from a python module **does not** give access to the dedicated graphics card. Some of the python modules are DLLs called PYD files. Importing pyd file with an exported _NvOptimusEnablement_ is not working properly.

The only solution I found so far is to create a python launcher that exports _NvOptimusEnablement_. From now on I am able to test my applications and games using the integrated and the dedicated graphics card as well.

Reference: [Optimus Rendering Policies](http://developer.download.nvidia.com/devzone/devcenter/gamegraphics/files/OptimusRenderingPolicies.pdf)

## How does it work?

The entire source code is in the [optimuspy.cpp](optimuspy.cpp).
The program simply passes every argument to the Py_Main.

To create a launcher for a specific application you can hardcode the parameters and add an icon using a resource file.

## Install

The [build.py](build.py) will detect the python installation and use the proper compiler arguments to create the optimuspy launcher.

Using the `--install` the `optimuspy.exe` will be placed next to the `python.exe`.

```batch
git clone https://github.com/cprogrammer1994/optimuspy
cd optimuspy
python build.py --install
```

### Compile using gcc

```batch
python build.py --gcc --install
```

## Sample

```batch
> python -m ModernGL

ModernGL: 4.1.11
Vendor: Intel
Renderer: Intel(R) HD Graphics 630
Version: 4.4.0 - Build 21.20.16.4541
```

```batch
> optimuspy -m ModernGL

ModernGL: 4.1.11
Vendor: NVIDIA Corporation
Renderer: GeForce GTX 1050/PCIe/SSE2
Version: 4.5.0 NVIDIA 384.94
```
