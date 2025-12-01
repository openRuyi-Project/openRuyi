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

Requires:       libsysfs = %{version}-%{release}

%description
This package's purpose is to provide a set of utilities for interfacing
with sysfs.

%package     -n libsysfs
Summary:        Shared library for interfacing with sysfs
License:        LGPL-2.1-or-later

%description -n libsysfs
Library used in handling linux kernel sysfs mounts and their various files.

%package     -n libsysfs-devel
Summary:        Static library and headers for libsysfs
License:        LGPL-2.1-or-later
Requires:       libsysfs = %{version}-%{release}

%description -n libsysfs-devel
libsysfs-devel provides the header files and static libraries required
to build programs using the libsysfs API.

%conf -p
autoreconf -fiv

%install -a
find %{buildroot} -type f -name "*.la" -delete

%files
%license COPYING cmd/GPL
%doc AUTHORS README CREDITS docs/libsysfs.txt
%{_bindir}/systool
%{_mandir}/man1/systool.1.gz

%files -n libsysfs
%license COPYING lib/LGPL
%{_libdir}/libsysfs.so.*

%files -n libsysfs-devel
%dir %{_includedir}/sysfs
%{_includedir}/sysfs/libsysfs.h
%{_includedir}/sysfs/dlist.h
%{_libdir}/libsysfs.so
%{_libdir}/pkgconfig/libsysfs.pc

%changelog
%{?autochangelog}
