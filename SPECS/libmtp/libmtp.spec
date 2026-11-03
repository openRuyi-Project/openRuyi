# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmtp
Version:        1.1.23
Release:        %autorelease
Summary:        Software library for MTP media players
License:        LGPL-2.1-or-later
URL:            https://github.com/libmtp/libmtp
#!RemoteAsset:  sha256:93ba3f860805f793ffaec3886ed5a2c1ea0a2e0407974c1d1b732d4d38ce34bc
Source0:        https://github.com/libmtp/libmtp/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

# fix non-root ignore --with-udev.
Patch0:         0001-fix-configure.patch
# https://github.com/libmtp/libmtp/commit/95d5c888520c296b1aac805e26e72d38648f4a80
Patch1000:      1000-ptp_free_objectpropdesc-NULL-freed-pointers.patch
# https://github.com/libmtp/libmtp/commit/7c29b868dba17ba0224a26f0998536137c7c013a
Patch1001:      1001-handle-return-code-of-OPD-unpack.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-doxygen
BuildOption(conf):  --with-udev=/usr/lib/udev

BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  doxygen

%description
This package provides a software library for communicating with MTP
(Media Transfer Protocol) media players, typically audio players, video
players etc.

%package        devel
Summary:        Development files for libmtp
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides development files for the libmtp library.

%conf -p
export ACLOCAL_PATH=%{_datadir}/gettext/m4/
./autogen.sh

%files
%doc AUTHORS README TODO
%license COPYING
%{_libdir}/libmtp.so.*
%{_udevrulesdir}/69-libmtp.rules
%{_prefix}/lib/udev/hwdb.d/69-libmtp.hwdb
%{_prefix}/lib/udev/mtp-probe
%{_bindir}/mtp-*
%{_docdir}/libmtp-%{version}/

%files devel
%{_libdir}/libmtp.so
%{_includedir}/libmtp.h
%{_libdir}/pkgconfig/libmtp.pc

%changelog
%autochangelog
