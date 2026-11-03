# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zopfli
Version:        1.0.3
Release:        %autorelease
Summary:        DEFLATE compressor and PNG optimizer
License:        Apache-2.0 AND Zlib
URL:            https://github.com/google/zopfli
#!RemoteAsset:  sha256:e955a7739f71af37ef3349c4fa141c648e8775bceb2195be07e86f8e638814bd
Source0:        %{url}/archive/refs/tags/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# Upstream LodePNG update caps decompression of PNG text and ICC metadata.
# https://github.com/google/zopfli/commit/005877c53e19f3913cd9d99d14bf18ef82ac474a
Patch1000:      1000-update-lodepng.patch

BuildOption(prep):  -n %{name}-%{name}-%{version}
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
BuildOption(conf):  -DZOPFLI_BUILD_SHARED=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Zopfli encodes DEFLATE, gzip and zlib streams. ZopfliPNG optimizes
PNG images and exposes its optimizer through a C and C++ interface.

%package        devel
Summary:        Development files for Zopfli and ZopfliPNG
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and build metadata for embedding the compression and PNG libraries.

%files
%doc README*
%license COPYING
%{_bindir}/zopfli
%{_bindir}/zopflipng
%{_libdir}/libzopfli.so.*
%{_libdir}/libzopflipng.so.*

%files devel
%{_includedir}/zopfli.h
%{_includedir}/zopflipng_lib.h
%{_libdir}/libzopfli.so
%{_libdir}/libzopflipng.so
%{_libdir}/cmake/Zopfli/

%changelog
%autochangelog
