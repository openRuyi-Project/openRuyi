# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global sover 0

Name:           xxhash
Version:        0.8.3
Release:        %autorelease
Summary:        Extremely fast non-cryptographic hash algorithm
License:        BSD-2-Clause AND GPL-2.0-only
URL:            https://cyan4973.github.io/xxHash/
#!RemoteAsset
Source0:        https://github.com/Cyan4973/xxHash/archive/v%{version}/%{name}-v%{version}.tar.gz

# Patch0: Fix build failures on non-x86 arches with DISPATCH=1 enabled
Patch0:         xxhash-fix-non-x86-dispatch.patch
# Patch1: Ensure test suite respects distro CFLAGS for security hardening
Patch1:         xxhash-test-respect-cflags.patch

BuildSystem:    autotools

BuildOption(build): DISPATCH=1
BuildOption(install): PREFIX=%{_prefix}
BuildOption(install): BINDIR=%{_bindir}
BuildOption(install): LIBDIR=%{_libdir}

BuildRequires:  gcc, make, autoconf, automake, libtool
BuildRequires:  pkgconfig

%description
xxHash is an extremely fast non-cryptographic hash algorithm, working at RAM
speed limits. It is used in many high-performance applications and libraries.

%package devel
Summary:        Development files for the xxHash library
License:        BSD-2-Clause
Requires:       xxhash = %{version}-%{release}

%description devel
This package contains the headers, pkg-config file, and symbolic links
necessary for developing applications that use the xxHash library.

%conf

%install -a

rm -f %{buildroot}%{_libdir}/libxxhash.a

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/libxxhash.so.%{sover}
%{_libdir}/libxxhash.so.%{sover}.*

%files devel
%{_includedir}/*.h
%{_libdir}/libxxhash.so
%{_libdir}/pkgconfig/libxxhash.pc

%changelog
%{?autochangelog}
