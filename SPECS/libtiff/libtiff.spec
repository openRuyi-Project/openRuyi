# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libtiff
Version:        4.7.0
Release:        %autorelease
Summary:        Tools for Converting from and to the Tagged Image File Format
License:        HPND
URL:            https://libtiff.gitlab.io/libtiff/
VCS:            git:https://gitlab.com/libtiff/libtiff
#!RemoteAsset
Source:         https://download.osgeo.org/libtiff/tiff-%{version}.tar.xz
BuildSystem:    cmake

Patch0:         libtiff-4.0.3-seek.patch
Patch1:         libtiff-4.7.0-test_directory.patch

# tools are not enabled for now due to test failure `FAIL: tiffcp-32bpp-None-jpeg.sh`
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  libtool
BuildRequires:  lzma-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

Recommends:     libtiff-docs = %{version}-%{release}

%description
This package contains the library and support programs for the TIFF
image format. To link a program with libtiff, you will have to add
-ljpeg and -lz to include the necessary libjpeg and libz in the
linking process.

%package        devel
Summary:        Development Tools for Programs which will use the libtiff Library
Requires:       glibc-devel
Requires:       libstdc++-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

Recommends:     libtiff-docs = %{version}

%description    devel
This package contains the header files and static libraries for
developing programs which will manipulate TIFF format image files using
the libtiff library.

%package        docs
Summary:        Libtiff HTML document
BuildArch:      noarch

%description    docs
This package holds libtiff command lint tools and development HTML pages.

%conf -p
CFLAGS="%{optflags} -fPIC"

%files
%{_bindir}/*
%doc README.md VERSION ChangeLog TODO RELEASE-DATE
%license LICENSE.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/tiff/

%files docs
%{_datadir}/doc/tiff

%changelog
%autochangelog
