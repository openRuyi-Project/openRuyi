# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <uwu@icenowy.me>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Mesa upstream now prohibits building w/ LTO
%global _lto_cflags %{nil}
# Mesa contains some features not applicable to Linux that must be disabled
%global __meson_auto_features disabled

Name:           mesa
Summary:        The Mesa 3D graphics library
Version:        26.0.1
Release:        %autorelease
License:        MIT
URL:            https://mesa3d.org/
VCS:            git:https://gitlab.freedesktop.org/mesa/mesa
#!RemoteAsset
Source:         https://archive.mesa3d.org/mesa-%{version}.tar.xz
BuildSystem:    meson

# Fixes etnaviv disasm unit test failure of excepting "-nan"
Patch1:         0001-isaspec-deocde-try-to-preserve-NaN-sign-when-printin.patch
# Patches to allow Zink running on libVK_IMG w/o IMG GLES driver
# See FD.o gitlab mesa/mesa MRs: !37115 !38810
# The IMG blob related part isn't submitted yet
Patch2:         mesa-26.0.1-zink-kmsro-for-img-blob.patch

# nvk is blocked by Rust packaging
BuildOption(conf):  -Dgallium-drivers=llvmpipe,softpipe,r300,r600,radeonsi,nouveau,virgl,iris,etnaviv,zink
BuildOption(conf):  -Dvulkan-drivers=amd,intel,swrast,imagination,virtio,gfxstream
BuildOption(conf):  -Dplatforms=x11,wayland

BuildOption(conf):  -Degl=enabled
BuildOption(conf):  -Dglx=dri
BuildOption(conf):  -Dgles1=enabled
BuildOption(conf):  -Dgles2=enabled
BuildOption(conf):  -Dopengl=true
BuildOption(conf):  -Dgbm=enabled
BuildOption(conf):  -Dglvnd=enabled

BuildOption(conf):  -Dllvm=enabled
BuildOption(conf):  -Dshared-llvm=enabled
BuildOption(conf):  -Ddraw-use-llvm=true
BuildOption(conf):  -Damd-use-llvm=true
BuildOption(conf):  -Dllvm-orcjit=true

BuildOption(conf):  -Dxmlconfig=enabled
BuildOption(conf):  -Dexpat=enabled
BuildOption(conf):  -Dshader-cache=enabled
BuildOption(conf):  -Dvalgrind=disabled
BuildOption(conf):  -Dlibunwind=enabled
BuildOption(conf):  -Dlmsensors=enabled
BuildOption(conf):  -Dzlib=enabled
BuildOption(conf):  -Dzstd=enabled
BuildOption(conf):  -Dallow-kcmp=enabled
BuildOption(conf):  -Dspirv-tools=enabled
BuildOption(conf):  -Ddisplay-info=enabled

# FIXME:  enable it when Rust dependency packaging is ready
BuildOption(conf):  -Dgallium-rusticl=false
BuildOption(conf):  -Dgallium-va=enabled

BuildOption(conf):  -Dvulkan-manifest-per-architecture=false
BuildOption(conf):  -Dvulkan-layers=device-select,overlay,screenshot,anti-lag,vram-report-limit
BuildOption(conf):  -Dxlib-lease=enabled

BuildRequires:  meson
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(mako)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(pycparser)
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  glslang
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_amdgpu)
BuildRequires:  pkgconfig(libdrm_intel)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libclc)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(LLVMSPIRVLib)
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(x11) >= 1.6
BuildRequires:  pkgconfig(xcb) >= 1.13
BuildRequires:  pkgconfig(xrandr) >= 1.3
BuildRequires:  pkgconfig(glproto) >= 1.4.14
BuildRequires:  pkgconfig(xshmfence) >= 1.1
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  lm_sensors-devel
BuildRequires:  zstd-devel
BuildRequires:  llvm-devel
BuildRequires:  clang-devel

%description
Mesa is a 3D graphics library containing implementation of OpenGL (along with
related APIs such as OpenGL ES / EGL), Vulkan and some other arbitary
acceleration APIs (e.g. libva).

%package     -n libgbm
Summary:        The GBM buffer management library

%description -n libgbm
GBM is a graphics buffer management library mainly for allocating graphics
buffers without the invocation of window systems (useful for display servers
themselves, headless multiple-application graphics acceleration, etc).

This package contains the libgbm entry point library, which just behaves as
a loader of different backends. Backends are provided by either Mesa or
other proprietary vendors.

%package     -n libgbm-devel
Summary:        Development files for libgbm
Requires:       libgbm = %{version}-%{release}

%description -n libgbm-devel
This package contains development files for libgbm, for either calling it or
implementing backends for it.

%package        drirc
Summary:        The default drirc configuration files
BuildArch:      noarch

%description    drirc
This package contains the default drirc configuration files for Mesa, which
behave as an application quirk database.

%package        gallium
Summary:        The core gallium driver file
# Open code to allow any version of drirc, for mixing gallium part and
# vulkan part from different Mesa releases if needed
Requires:       %{name}-drirc

%description    gallium
This package contains a shared library that holds all core code for gallium
drivers (GL/DRI loader/others).

%package        gl
Summary:        The gallium-based GL driver
Requires:       %{name}-gallium = %{version}-%{release}

%description    gl
This package contains the implementation of GL-related APIs (Desktop OpenGL,
OpenGL ES, EGL and GLX) based on Gallium, along with the dri gbm backend,
which is coupled with the EGL implementation.

%package        gl-ext-headers
Summary:        Extra headers for Mesa EGL extensions
BuildArch:      noarch

%description    gl-ext-headers
This package contains extra headers with definitions for some EGL extensions
implemented by Mesa, which are not available from Khronos.

%package        dril
Summary:        The gallium DRI loader entry libraries
Requires:       %{name}-gl = %{version}-%{release}

%description    dril
This package contains DRI loader entry libraries, which are available for
X.org server to implement AIGLX.

%package        dril-devel
Summary:        The gallium DRI loader development files
Requires:       %{name}-dril = %{version}-%{release}
BuildArch:      noarch

%description    dril-devel
This package contains development-related files for the DRI loader interface,
including a header file describing the interface and a pkgconfig file.

%package        va
Summary:        The gallium-based libva hardware video codec driver
Requires:       %{name}-gallium = %{version}-%{release}

%description    va
This package contains libva drivers based on Gallium.

%package        vulkan-drivers
Summary:        Vulkan drivers provided by Mesa
# See the comment at gallium subpackage above about why open-coding version
Requires:       %{name}-drirc

%description    vulkan-drivers
This package contains Vulkan drivers provided as part of Mesa project, which
are to be loaded by the Khronos Vulkan loader.

%package        vulkan-layers
Summary:        Vulkan layers provided by Mesa

%description    vulkan-layers
This package contains Vulkan layers provided as part of Mesa project, which
are to be loaded by the Khronos Vulkan loader, and can be used even for
non-Mesa drivers.

%files -n libgbm
%{_libdir}/libgbm.so.1*

%files -n libgbm-devel
%{_libdir}/libgbm.so
%{_includedir}/gbm.h
%{_includedir}/gbm_backend_abi.h
%{_libdir}/pkgconfig/gbm.pc

%files drirc
%{_datadir}/drirc.d/*.conf

%files gallium
%{_libdir}/libgallium-%{version}.so

%files gl
%{_libdir}/libEGL_mesa.so*
%{_libdir}/libGLX_mesa.so*
%{_libdir}/gbm/dri_gbm.so
%{_datadir}/glvnd/egl_vendor.d/50_mesa.json

%files gl-ext-headers
%{_includedir}/EGL/eglext_angle.h
%{_includedir}/EGL/eglmesaext.h

%files dril
%{_libdir}/dri/*_dri.so

%files dril-devel
%{_includedir}/GL/internal/dri_interface.h
%{_libdir}/pkgconfig/dri.pc

%files va
%{_libdir}/dri/*_drv_video.so

%files vulkan-drivers
%{_libdir}/libvulkan_*.so
%{_datadir}/vulkan/icd.d/*.json

%files vulkan-layers
%{_libdir}/libVkLayer_*.so
%{_datadir}/vulkan/*_layer.d/*.json
%{_bindir}/mesa-*-control.py

%changelog
%autochangelog
