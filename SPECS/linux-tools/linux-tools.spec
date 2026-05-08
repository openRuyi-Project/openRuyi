# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0
%bcond doc 0

Name:           linux-tools
Version:        7.0.5
Release:        %autorelease
Summary:        Set of tools for the Linux kernel
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-only
URL:            https://www.kernel.org/
VCS:            git:https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
#!RemoteAsset:  sha256:965fb0a1c1675399fc60c6063b227c0523041b5f9a662b66462f1212c438ac3c
Source0:        https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-%{version}.tar.xz

%if %{with doc}
BuildRequires:  asciidoc
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext-tools
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(libdwarf)
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sysfsutils
BuildRequires:  xmlto
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libtraceevent)
BuildRequires:  pkgconfig(libdebuginfod)
BuildRequires:  systemtap-sdt-devel
BuildRequires:  clang
BuildRequires:  pkgconfig(slang)
BuildRequires:  python3-setuptools
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig(numa)
BuildRequires:  systemd-rpm-macros

%description
This package contains the tools/ directory from the kernel source
and the supporting documentation.

%package        devel
Summary:        Development files for %{name}
License:        GPL-2.0-only
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries and header files for the
tools/ directory from the kernel source.

%package     -n perf
Summary:        Performance monitoring for the Linux kernel
License:        GPL-2.0-only

%description -n perf
This package contains the perf tool, which enables performance monitoring
of the Linux kernel.

%prep
%autosetup -p1 -n linux-%{version}

%build
%make_build -C tools EXTRA_CFLAGS="%{optflags}" bootconfig gpio iio spi tmon

%make_build -C tools LD=ld.bfd EXTRA_CFLAGS="%{optflags} -Wno-array-bounds -Wno-maybe-uninitialized" perf

%make_build -C tools/power/cpupower EXTRA_CFLAGS="%{optflags}" CPUFRQ_BENCH=false VERSION=%{version}

pushd tools/usb/usbip
./autogen.sh
%configure --disable-static
%make_build
popd

%install
make -C tools/power/cpupower DESTDIR=%{buildroot} libdir=%{_libdir} mandir=%{_mandir} CPUFREQ_BENCH=false VERSION=%{version} install

make -C tools DESTDIR=%{buildroot} bootconfig_install gpio_install iio_install spi_install

make -C tools INSTALL_ROOT=%{buildroot} tmon_install

make -C tools/perf LD=ld.bfd EXTRA_CFLAGS="%{optflags} -Wno-array-bounds -Wno-maybe-uninitialized" DESTDIR=%{buildroot} prefix=%{_prefix} install-bin

make -C tools/usb/usbip DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -type f -name "*.a" -delete -print

%find_lang cpupower --generate-subpackages

%files
%license COPYING
%{_bindir}/cpupower
%{_mandir}/man1/cpupower*
%{_datadir}/bash-completion/completions/cpupower
%config %{_sysconfdir}/cpupower-service.conf
%{_unitdir}/cpupower.service
%{_libexecdir}/cpupower
%{_libdir}/libcpupower.so*.1
%{_bindir}/bootconfig
%{_bindir}/spidev_*
%{_bindir}/tmon
%{_bindir}/iio_event_monitor
%{_bindir}/iio_generic_buffer
%{_bindir}/lsiio
%{_bindir}/gpio-*
%{_bindir}/lsgpio
%{_sbindir}/usbip
%{_sbindir}/usbipd
%{_mandir}/man8/usbip.8*
%{_mandir}/man8/usbipd.8*
%{_libdir}/libusbip.so.0*

%files devel
%{_libdir}/libcpupower.so
%{_includedir}/cpufreq.h
%{_includedir}/cpuidle.h
%{_includedir}/powercap.h
%dir %{_includedir}/usbip
%{_includedir}/usbip/*.h
%{_libdir}/libusbip.so

%files -n perf
%license COPYING
%{_bindir}/perf
%{_bindir}/trace
%{_libexecdir}/perf-core
%{_sysconfdir}/bash_completion.d/perf
%{_docdir}/perf-tip/tips.txt
%{_includedir}/perf/perf_dlfilter.h

%changelog
%autochangelog
