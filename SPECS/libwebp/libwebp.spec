# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:          libwebp
Version:       1.6.0
Release:       %autorelease
Summary:       Library and tools for the WebP graphics format
License:       Apache-2.0 AND BSD-3-Clause
URL:           https://github.com/webmproject/libwebp
#!RemoteAsset
Source:        https://github.com/webmproject/libwebp/archive/refs/tags/v%{version}.tar.gz
Patch0:        0001-libwebp-cmakedir.patch
Patch1:        0002-libwebp-rpath.patch
BuildSystem:   cmake

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: giflib-devel
BuildRequires: pkgconfig(libjpeg)
BuildRequires: libpng-devel
BuildRequires: libtiff-devel

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. This package contains the runtime libraries.

%package       tools
Summary:       The WebP command line tools
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   tools
The %{name}-tools package contains the WebP command line tools (cwebp,
dwebp, etc.) for encoding and decoding WebP images.

%package       devel
Summary:       Development files for libwebp
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license COPYING
%doc README.md PATENTS NEWS AUTHORS
%{_libdir}/libwebp.so.7*
%{_libdir}/libwebpdecoder.so.3*
%{_libdir}/libwebpdemux.so.2*
%{_libdir}/libwebpmux.so.3*
%{_libdir}/libsharpyuv.so.0*

%files tools
%{_bindir}/cwebp
%{_bindir}/dwebp
%{_bindir}/gif2webp
%{_bindir}/img2webp
%{_bindir}/webpinfo
%{_bindir}/webpmux
%{_mandir}/man*/*

%files devel
%{_libdir}/libwebp.so
%{_libdir}/libwebpdecoder.so
%{_libdir}/libwebpdemux.so
%{_libdir}/libwebpmux.so
%{_libdir}/libsharpyuv.so
%{_includedir}/webp/
%{_libdir}/pkgconfig/libwebp.pc
%{_libdir}/pkgconfig/libwebpdecoder.pc
%{_libdir}/pkgconfig/libwebpdemux.pc
%{_libdir}/pkgconfig/libwebpmux.pc
%{_libdir}/pkgconfig/libsharpyuv.pc
%{_libdir}/cmake/WebP/

%changelog
%{?autochangelog}
