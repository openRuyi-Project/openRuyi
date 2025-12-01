# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pciutils
Version:        3.14.0
Release:        %autorelease
Summary:        PCI utilities for the Linux Kernel
License:        GPL-2.0-or-later
URL:            https://mj.ucw.cz/sw/pciutils/
#!RemoteAsset
Source:         https://www.kernel.org/pub/software/utils/pciutils/pciutils-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(build):   OPT="%{optflags}"
BuildOption(build):   PREFIX=%{_prefix}
BuildOption(build):   LIBDIR=%{_libdir}
BuildOption(build):   SBINDIR=%{_sbindir}
BuildOption(build):   STRIP=""
BuildOption(build):   SHARED="yes"

BuildOption(install): install-lib
BuildOption(install): PREFIX=%{_prefix}
BuildOption(install): SBINDIR=%{_sbindir}
BuildOption(install): ROOT=""
BuildOption(install): MANDIR=%{_mandir}
BuildOption(install): STRIP=""
BuildOption(install): SHARED="yes"
BuildOption(install): LIBDIR=%{_libdir}

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(zlib)
Requires:       hwdata

%description
This package contains command-line utilities for inspecting and manipulating
devices connected to the PCI bus.

%package devel
Summary:        Development files for the PCI utilities
Requires:       %{name} = %{version}

%description devel
This package contains the header files and development files for the
PCI utilities library.

# No configure
%conf

%install -a
install -d -m 755 %{buildroot}%{_includedir}/pci
install -m 644 lib/pci.h lib/header.h lib/config.h lib/types.h %{buildroot}%{_includedir}/pci/
install -D -m 644 lib/libpci.pc %{buildroot}%{_libdir}/pkgconfig/libpci.pc
(cd %{buildroot}%{_libdir} && ln -sf libpci.so.3 libpci.so)

# No tests
%check

%files
%license COPYING
%doc README
%{_bindir}/lspci
%{_sbindir}/pcilmr
%{_sbindir}/setpci
%{_sbindir}/update-pciids
%{_mandir}/man*/*
%{_libdir}/libpci.so.3
%{_libdir}/libpci.so.3.*
%{_datadir}/pci.ids*

%files devel
%{_includedir}/pci/
%{_libdir}/pkgconfig/libpci.pc
%{_libdir}/libpci.so

%changelog
%{?autochangelog}
