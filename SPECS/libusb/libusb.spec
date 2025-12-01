# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libusb
Version:        1.0.29
Release:        %autorelease
Summary:        Public client interface library for NIS(YP) and NIS+
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            http://libusb.info
VCS:            git:https://github.com/libusb/libusb
#!RemoteAsset
Source0:        https://github.com/libusb/libusb/releases/download/v%{version}/%{name}-%{version}.tar.bz2
#!RemoteAsset
Source1:        https://github.com/libusb/libusb/releases/download/v%{version}/%{name}-%{version}.tar.bz2.asc
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libsystemd)

%description
This package provides a way for applications to access USB devices.

libusb is a library for USB device access from Linux, macOS,
Windows, OpenBSD/NetBSD, Haiku and Solaris userspace.

libusb is abstracted internally in such a way that it can hopefully
be ported to other operating systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
autoreconf -fiv

%install -a
rm %{buildroot}%{_libdir}/*.la

%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_libdir}/*.so.*

%files devel
%{_includedir}/libusb-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/libusb-1.0.pc

%changelog
%{?autochangelog}
