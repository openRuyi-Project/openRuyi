# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           qrencode
Version:        4.1.1
Release:        %autorelease
Summary:        Generate QR 2D barcodes
License:        LGPL-2.1-or-later
URL:            https://github.com/fukuchi/libqrencode
#!RemoteAsset:  sha256:5385bc1b8c2f20f3b91d258bf8ccc8cf62023935df2d2676b5b67049f31a049c
Source0:        https://github.com/fukuchi/libqrencode/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --with-tests
BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libpng)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Qrencode is a utility software using libqrencode to encode string data in
a QR Code and save as a PNG image.

%package        devel
Summary:        QR Code encoding library - Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The qrencode-devel package contains libraries and header files for developing
applications that use qrencode.

%conf -p
./autogen.sh

%files
%license COPYING
%doc ChangeLog NEWS README TODO
%{_bindir}/qrencode
%{_mandir}/man1/qrencode.1*
%{_libdir}/libqrencode.so.*

%files devel
%{_includedir}/qrencode.h
%{_libdir}/libqrencode.so
%{_libdir}/pkgconfig/libqrencode.pc

%changelog
%autochangelog
