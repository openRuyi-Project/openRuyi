# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnvme
Version:        1.16.1
Release:        %autorelease
Summary:        Linux-native nvme device management library
License:        LGPL-2.1-or-later
URL:            https://github.com/linux-nvme/libnvme
#!RemoteAsset:  sha256:ce1d9d393feb84c4e82ca096db2bdb7dd4a5fd1997d711cc1904796944f2c579
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Ddocs=man

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  swig
BuildRequires:  python3-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(openssl)

%description
libnvme provides type definitions for NVMe specification structures,
enumerations, and bit fields, helper functions to construct, dispatch,
and decode commands and payloads, and utilities to connect, scan, and
manage nvme devices on a Linux system.

%package        devel
Summary:        Development files for Linux-native nvme
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides header files to include and libraries to link with
for Linux-native nvme device maangement.

%package        help
Summary:        Reference manual for libnvme
BuildArch:      noarch

%description    help
This package contains the reference manual for %{name}.

%package     -n python-libnvme
Summary:        Python bindings for libnvme
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-nvme = %{version}-%{release}
%{?python_provie:%python_provide python3-libnvme}

%description -n python-libnvme
This package contains Python binding for libnvme.

%files
%license COPYING
%doc README.md
%{_libdir}/libnvme.so.*
%{_libdir}/libnvme-mi.so.*

%files devel
%{_libdir}/libnvme.so
%{_libdir}/libnvme-mi.so
%{_includedir}/libnvme.h
%{_includedir}/libnvme-mi.h
%dir %{_includedir}/nvme
%{_includedir}/nvme/*
%{_libdir}/pkgconfig/libnvme-mi.pc
%{_libdir}/pkgconfig/libnvme.pc

%files help
%{_mandir}/man2/*

%files -n python-libnvme
%dir %{python3_sitearch}/libnvme
%{python3_sitearch}/libnvme/*

%changelog
%autochangelog
