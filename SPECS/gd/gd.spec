# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# To enable these, change to 1
%bcond avif 0
%bcond webp 0
%bcond xpm 0

Name:           gd
Version:        2.3.3
Release:        %autorelease
Summary:        A Drawing Library for Programs That Use PNG and JPEG Output
License:        MIT
URL:            http://libgd.github.io/
VCS:            git:https://github.com/libgd/libgd
#!RemoteAsset
Source0:        https://github.com/libgd/libgd/releases/download/%{name}-%{version}/libgd-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-werror
BuildOption(conf):  --disable-slient-rules
BuildOption(conf):  --without-liq
BuildOption(conf):  --without-x
BuildOption(conf):  --with-fontconfig
BuildOption(conf):  --with-freetype
BuildOption(conf):  --with-jpeg
BuildOption(conf):  --with-png
%if %{with avif}
BuildOption(conf):  --with-avif
%endif
%if %{with webp}
BuildOption(conf):  --with-webp
%endif
%if %{with xpm}
BuildOption(conf):  --with-xpm
%endif

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
%if %{with avif}
BuildRequires:  pkgconfig(libavif)
%endif
%if %{with webp}
BuildRequires:  pkgconfig(libwebp)
%endif
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
%if %{with xpm}
BuildRequires:  pkgconfig(xpm)
%endif
# Tests
BuildRequires:  fonts-dejavu

Provides:       gdlib = %{version}

%description
The gd graphics library allows your code to quickly draw images
complete with lines, arcs, text, multiple colors, cut and paste from
other images, and flood fills, and to write out the result as a PNG or
JPEG file. This is particularly useful in Web applications, where PNG
and JPEG are two of the formats accepted for inline images by most
browsers. Note that gd is not a paint program.

%package        devel
Summary:        The development libraries and header files for gd
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the development libraries and header files
for gd, a graphics library for creating PNG and JPEG graphics.

%conf -p
autoreconf -fiv
%ifnarch x86_64
export CFLAGS="%{build_cflags} -ffp-contract=off"
%endif

%check -p
# https://github.com/libgd/libgd/issues/763#issuecomment-918049103
export TMPDIR=/tmp

%files
%doc README.md
%license COPYING
%{_bindir}/annotate
%{_bindir}/bdftogd
%{_bindir}/gd2copypal
%{_bindir}/gd2togif
%{_bindir}/gd2topng
%{_bindir}/gdcmpgif
%{_bindir}/gdparttopng
%{_bindir}/gdtopng
%{_bindir}/giftogd2
%{_bindir}/pngtogd
%{_bindir}/pngtogd2
%{_bindir}/webpng

%files devel
%license COPYING
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_libdir}/pkgconfig/gdlib.pc

%changelog
%autochangelog
