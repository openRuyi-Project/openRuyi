# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Han Gao <gaohan@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Hangfan Li <lihangfan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond tools 1
%bcond rust  1

# Whether dtbs needed for arch
%ifarch riscv64
%global need_dtbs 1
%else
%global need_dtbs 0
%endif

%global _lto_cflags %{nil}

#### About Versioning
#
# CONFIG_LOCALVERSION_AUTO must not be set.
# This ensures kernel build system never injects hash value generated from commit id.
# This also bypass the KBUILD_BUILD_VERSION logic.
#

# Making flavored kernels by setting this one.
# This will be included into `uname -r` so that multiple kernels will co-exist
# %%global variant_name

# SHOULD NOT TOUCH
%global kernel_local_version    %{?variant_name:%{variant_name}-}%{release}
%global kernel_full_version     %{version}-%{kernel_local_version}

%global kernel_make_flags LD=ld.bfd
%global modpath /lib/modules/%{kernel_full_version}

Name:           linux
Version:        7.1.3
Release:        %autorelease
Summary:        The Linux Kernel
License:        GPL-2.0-only
URL:            https://www.kernel.org/
#!RemoteAsset:  sha256:be41c068e88f5242a19bccdbffbe077b18c47b45f627e2325504b4fab79dd1dc
Source0:        https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-%{version}.tar.xz
Source1:        config.%{_arch}
Source2:        series

BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  binutils
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  flex
BuildRequires:  bc
BuildRequires:  cpio
BuildRequires:  dwarves
BuildRequires:  gettext
BuildRequires:  python3
BuildRequires:  rsync
BuildRequires:  tar
BuildRequires:  xz
BuildRequires:  zstd
BuildRequires:  libdebuginfod-dummy-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(slang)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  kmod
BuildRequires:  rpm-config-openruyi
%if %{with tools}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  clang
BuildRequires:  libtool
BuildRequires:  pkgconfig(babeltrace)
BuildRequires:  pkgconfig(capstone)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libtraceevent)
BuildRequires:  pkgconfig(numa)
BuildRequires:  python3dist(setuptools)
BuildRequires:  systemtap-sdt-devel
%endif
%if %{with rust}
BuildRequires:  bindgen
BuildRequires:  cargo
BuildRequires:  rust
%endif

# Meta-package: default installation
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-modules%{?_isa} = %{version}-%{release}
%if %{need_dtbs}
Requires:       %{name}-dtbs%{?_isa} = %{version}-%{release}
%endif

# Meta-package: order of removal
Requires(preun): %{name}-core%{?_isa} = %{version}-%{release}
Requires(preun): %{name}-modules%{?_isa} = %{version}-%{release}
%if %{need_dtbs}
Requires(preun): %{name}-dtbs%{?_isa} = %{version}-%{release}
%endif

Requires(post):   kernel-install
Requires(preun):  kernel-install

%patchlist
%include %{SOURCE2}

%description
This is a meta-package that handles standard kernel installation.
To avoid the execution of kernel service scriptlet, please install
%{name}-core%{?_isa}, %{name}-modules%{?_isa} instead.

%package        core
Summary:        The core Linux kernel image

%description    core
Contains the bootable kernel image (vmlinuz) and its Kconfig options.

%package        modules
Summary:        Kernel modules for the Linux kernel
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    modules
Contains all the kernel modules (.ko files) and associated metadata for
the hardware drivers and kernel features.

%package        devel
Summary:        Development files for building external kernel modules
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dwarves

%description    devel
This package provides the kernel headers and Makefiles necessary to build
external kernel modules against the installed kernel. The development files are
located at %{_usrsrc}/kernels/%{kernel_full_version}, with symlinks provided under
/lib/modules/%{kernel_full_version}/ for compatibility.

%if %{with tools}
%package        tools
Summary:        Set of tools for the Linux kernel
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-only
Provides:       perf = %{version}-%{release}
Obsoletes:      perf < %{version}-%{release}

%description    tools
This package contains the tools/ directory from the kernel source
and the supporting documentation.

%package        tools-devel
Summary:        Development files for %{name}
License:        GPL-2.0-only
Requires:       %{name}-tools%{?_isa} = %{version}-%{release}

%description    tools-devel
This package contains the libraries and header files for the
tools/ directory from the kernel source.
%endif

%if %{need_dtbs}
%package        dtbs
Summary:        Devicetree blob files from Linux sources
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    dtbs
This package provides the DTB files built from Linux sources that may be used
for booting.
%endif

%prep
%autosetup -p1
cp %{SOURCE1} .config
echo "-%{kernel_local_version}" > localversion

%conf
%make_build %{kernel_make_flags} olddefconfig

%build
%if %{with tools}
# build tools
%make_build -C tools EXTRA_CFLAGS="%{optflags}" bootconfig gpio iio spi tmon
%make_build -C tools LD=ld.bfd EXTRA_CFLAGS="%{optflags} -Wno-array-bounds -Wno-maybe-uninitialized" perf
%make_build -C tools/power/cpupower EXTRA_CFLAGS="%{optflags}" CPUFRQ_BENCH=false VERSION=%{version}

pushd tools/usb/usbip
./autogen.sh
%configure --disable-static
%make_build
popd
%endif

# build kernel

%make_build %{kernel_make_flags}

%if %{need_dtbs}
%make_build %{kernel_make_flags} dtbs
%endif

%install
%if %{with tools}
# install tools
make -C tools/power/cpupower DESTDIR=%{buildroot} libdir=%{_libdir} mandir=%{_mandir} CPUFREQ_BENCH=false VERSION=%{version} install
make -C tools DESTDIR=%{buildroot} bootconfig_install gpio_install iio_install spi_install
make -C tools INSTALL_ROOT=%{buildroot} tmon_install
make -C tools/perf LD=ld.bfd EXTRA_CFLAGS="%{optflags} -Wno-array-bounds -Wno-maybe-uninitialized" DESTDIR=%{buildroot} prefix=%{_prefix} install-bin
make -C tools/usb/usbip DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -type f -name "*.a" -delete -print
%find_lang cpupower --generate-subpackages
%endif

# install kernel

%define ksrcpath %{buildroot}%{_usrsrc}/kernels/%{kernel_full_version}
install -d %{buildroot}%{modpath} %{ksrcpath}

%make_build %{kernel_make_flags} INSTALL_MOD_PATH=%{buildroot} INSTALL_MOD_STRIP=1 DEPMOD=true modules_install

%if %{need_dtbs}
%make_build %{kernel_make_flags} INSTALL_DTBS_PATH=%{buildroot}%{modpath}/dtb dtbs_install
%endif

%make_build run-command %{kernel_make_flags} KBUILD_RUN_COMMAND="$(pwd)/scripts/package/install-extmod-build %{ksrcpath}"

pushd %{buildroot}%{modpath}
rm -f build source
ln -sf %{_usrsrc}/kernels/%{kernel_full_version} build
ln -sf %{_usrsrc}/kernels/%{kernel_full_version} source
popd

install -Dm644 $(make %{kernel_make_flags} -s image_name) %{buildroot}%{modpath}/vmlinuz
zstd -f .config -o %{buildroot}%{modpath}/config.zst

echo "Module signing would happen here for version %{kernel_full_version}."

%pretrans
# Cleanup state file ahead to avoid leftovers from previous failure.
rm -f "%{_localstatedir}/lib/rpm-state/%{name}-%{kernel_full_version}.just_installed"

%post
# Workaround reinstalling: let %%preun know that the same package is installed just before.
touch "%{_localstatedir}/lib/rpm-state/%{name}-%{kernel_full_version}.just_installed"

%{_bindir}/kernel-install add %{kernel_full_version} %{modpath}/vmlinuz

%preun
# Why not "if [ $1 -eq 0 ]"? It breaks kernel removal when multi versions were installed.
if [ ! -e "%{_localstatedir}/lib/rpm-state/%{name}-%{kernel_full_version}.just_installed" ]; then
    %{_bindir}/kernel-install remove %{kernel_full_version}
fi

%posttrans
rm -f "%{_localstatedir}/lib/rpm-state/%{name}-%{kernel_full_version}.just_installed"

%files
%license COPYING
%doc README

%files core
%dir %{modpath}
%{modpath}/vmlinuz
%{modpath}/config.zst

%files modules
%{modpath}/kernel
%{modpath}/modules.builtin
%{modpath}/modules.builtin.modinfo
%{modpath}/modules.order

%files devel
%{_usrsrc}/kernels/%{kernel_full_version}/
%{modpath}/build
%{modpath}/source

%if %{need_dtbs}
%files dtbs
%{modpath}/dtb
%endif

%if %{with tools}
# linux tools
%files tools -f cpupower.lang
%license COPYING
%config %{_sysconfdir}/cpupower-service.conf
%{_bindir}/bootconfig
%{_bindir}/cpupower
%{_bindir}/gpio-*
%{_bindir}/iio_event_monitor
%{_bindir}/iio_generic_buffer
%{_bindir}/lsgpio
%{_bindir}/lsiio
%{_bindir}/perf
%{_bindir}/spidev_*
%{_bindir}/tmon
%{_bindir}/trace
%{_datadir}/bash-completion/completions/cpupower
%{_libdir}/libcpupower.so*.1
%{_libdir}/libusbip.so.0*
%{_libexecdir}/cpupower
%{_libexecdir}/perf-core
%{_mandir}/man1/cpupower*
%{_mandir}/man8/usbip.8*
%{_mandir}/man8/usbipd.8*
%{_sbindir}/usbip
%{_sbindir}/usbipd
%{_sysconfdir}/bash_completion.d/perf
%{_unitdir}/cpupower.service

%files tools-devel
%dir %{_includedir}/perf
%dir %{_includedir}/usbip
%{_docdir}/perf-tip/tips.txt
%{_includedir}/cpufreq.h
%{_includedir}/cpuidle.h
%{_includedir}/perf/perf_dlfilter.h
%{_includedir}/powercap.h
%{_includedir}/usbip/*.h
%{_libdir}/libcpupower.so
%{_libdir}/libusbip.so
%endif

%changelog
%autochangelog
