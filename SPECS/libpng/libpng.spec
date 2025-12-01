# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Suyun114 <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libpng
Version:        1.6.50
Release:        %autorelease
Summary:        A library of functions for manipulating PNG image format files
License:        zlib
URL:            http://www.libpng.org/pub/png/
#!RemoteAsset
Source0:        https://github.com/glennrp/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:    autotools
BuildOption(conf):  --disable-static

BuildRequires:  zlib-devel

%description
The libpng package contains a library of functions for creating and
manipulating PNG (Portable Network Graphics) image format files.  PNG
is a bit-mapped graphics format similar to the GIF format.  PNG was
created to replace the GIF format, since GIF uses a patented data
compression algorithm.

Libpng should be installed if you need to manipulate PNG format image
files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
The libpng-devel package contains header files and documentation necessary
for developing programs using the PNG (Portable Network Graphics) library.

If you want to develop programs which will manipulate PNG image format
files, you should install libpng-devel.  You'll also need to install
the libpng package.

%files
%license LICENSE
%{_bindir}/pngfix
%{_libdir}/libpng*.so.*
%{_mandir}/man5/*

%files devel
%doc libpng-manual.txt example.c TODO CHANGES
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libpng*.so
%{_libdir}/pkgconfig/libpng*.pc
%{_mandir}/man3/*

%changelog
%{?autochangelog}
