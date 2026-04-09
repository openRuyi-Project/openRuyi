# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libspng
Version:        0.7.4
Release:        %autorelease
Summary:        Simple, modern libpng alternative
License:        BSD-2-Clause
URL:            https://libspng.org/
VCS:            git:https://github.com/randy408/libspng
#!RemoteAsset
Source0:        https://github.com/randy408/libspng/archive/v%{version}/libspng-%{version}.tar.gz
BuildSystem:    meson

# some patch should fail.
# spng incompatible with libpng 1.6.47 (PNGv3)
# https://github.com/randy408/libspng/issues/276
Patch0:         0001-tests-should-fail.patch

BuildOption(conf):  -Ddev_build=true

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)

%description
Libspng is a C library for reading and writing Portable Network Graphics (PNG)
format files with a focus on security and ease of use.

Libspng is an alternative to libpng, the projects are separate and the APIs are
not compatible. This package contains the runtime shared library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_libdir}/libspng.so.0
%{_libdir}/libspng.so.0.*

%ifarch riscv64
%check
# waiting to fix/check the feature in riscv64.
%endif

%files devel
%doc docs
%{_includedir}/spng.h
%{_libdir}/libspng.so
%{_libdir}/pkgconfig/spng.pc

%changelog
%autochangelog
