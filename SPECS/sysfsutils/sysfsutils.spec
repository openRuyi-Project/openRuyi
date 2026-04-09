# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sysfsutils
Version:        2.1.1
Release:        %autorelease
Summary:        Utilities for interfacing with sysfs
License:        GPL-2.0-only
URL:            https://github.com/linux-ras/sysfsutils
#!RemoteAsset
Source:         %{url}/archive/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc

# Compatibility provides
Provides:       libsysfs = %{version}-%{release}

%description
This package's purpose is to provide a set of utilities for interfacing
with sysfs.

%package        devel
Summary:        Static library and headers for libsysfs
License:        LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Compatibility provides
Provides:       libsysfs-devel = %{version}-%{release}

%description    devel
This package provides the header files and static libraries required
to build programs using the libsysfs API.

%conf -p
autoreconf -fiv

%files
%license COPYING cmd/GPL
%doc AUTHORS README CREDITS docs/libsysfs.txt
%{_bindir}/systool
%{_mandir}/man1/systool.1.gz
%{_libdir}/libsysfs.so.*

%files devel
%dir %{_includedir}/sysfs
%{_includedir}/sysfs/libsysfs.h
%{_includedir}/sysfs/dlist.h
%{_libdir}/libsysfs.so
%{_libdir}/pkgconfig/libsysfs.pc

%changelog
%autochangelog
