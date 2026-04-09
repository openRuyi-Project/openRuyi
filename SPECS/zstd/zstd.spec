# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond pzstd 0

Name:            zstd
Version:         1.5.7
Release:         %autorelease
Summary:         A fast lossless compression algorithm
License:         BSD-3-Clause AND GPL-2.0-only
URL:             https://github.com/facebook/zstd
#!RemoteAsset
Source:          https://github.com/facebook/zstd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Buildsystem:     autotools

BuildRequires:   gzip
BuildRequires:   gcc
BuildRequires:   gcc-c++
BuildRequires:   pkgconfig(liblz4)
BuildRequires:   pkgconfig(liblzma)
BuildRequires:   pkgconfig(zlib)
%if %{with pzstd}
BuildRequires:   pkgconfig(gtest)
%endif

Provides:        libzstd = %{version}-%{release}
Obsoletes:       libzstd < %{version}-%{release}

%description
Zstd is a fast lossless compression algorithm. It's backed by a very fast entropy stage,
provided by Huff0 and FSE library. It's a real-time compression scenario for zlib levels
and has a better compression ratio.

%package         devel
Summary:         Header files for zstd library
Requires:        %{name}%{?_isa} = %{version}-%{release}
Provides:        libzstd-devel = %{version}-%{release}
Obsoletes:       libzstd-devel < %{version}-%{release}
Provides:        libzstd-static = %{version}-%{release}
Obsoletes:       libzstd-static < %{version}-%{release}

%description     devel
This package contains the header files for zstd library.

%conf
:

%if %{with pzstd}
%build -a
%make_build -C contrib/pzstd CXXFLAGS="$RPM_OPT_FLAGS -std=c++11"
%endif

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
%if %{with pzstd}
install -D -m755 contrib/pzstd/pzstd %{buildroot}%{_bindir}/pzstd
install -D -m644 programs/zstd.1 %{buildroot}%{_mandir}/man1/pzstd.1
%endif

%files
%doc CHANGELOG README.md
%license LICENSE COPYING
%{_bindir}/*
%{_libdir}/libzstd.so.*
%{_mandir}/man1/*

%files devel
%{_includedir}/*.h
%{_libdir}/pkgconfig/libzstd.pc
%{_libdir}/libzstd.so
%{_libdir}/libzstd.a

%changelog
%autochangelog
