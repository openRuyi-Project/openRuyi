# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           potrace
Version:        1.16
Release:        %autorelease
Summary:        Transforming bitmaps into vector graphics
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            http://potrace.sourceforge.net
# VCS: No VCS link available
#!RemoteAsset:  sha256:be8248a17dedd6ccbaab2fcc45835bb0502d062e40fbded3bc56028ce5eb7acc
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-libpotrace

BuildRequires:  pkgconfig(zlib)
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Potrace is a utility for tracing a bitmap, which means, transforming a bitmap
into a smooth, scalable image. The input is a bitmap (PBM, PGM, PPM, or BMP
format), and the default output is one of several vector file formats. A typical
use is to create EPS files from scanned data, such as company or university
logos, handwritten notes, etc. The resulting image is not "jaggy" like a bitmap,
but smooth. It can then be rendered at any resolution.

%package        devel
Summary:        Library Development Files for Tracing a Bitmap to Scalable Outline Image
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Potrace is a utility for tracing a bitmap, which means, transforming a bitmap
into a smooth, scalable image. The input is a bitmap (PBM, PGM, PPM, or BMP
format), and the default output is one of several vector file formats. A typical
use is to create EPS files from scanned data, such as company or university
logos, handwritten notes, etc. The resulting image is not "jaggy" like a bitmap,
but smooth. It can then be rendered at any resolution.

This package includes the potrace development libraries.

%conf -p
autoreconf -fiv

%files
%doc AUTHORS ChangeLog COPYING NEWS README placement.pdf
%{_bindir}/potrace
%{_bindir}/mkbitmap
%{_libdir}/libpotrace.so.*
%{_mandir}/man1/potrace.1*
%{_mandir}/man1/mkbitmap.1*

%files devel
%{_libdir}/libpotrace.so
%{_includedir}/potracelib.h

%changelog
%autochangelog
