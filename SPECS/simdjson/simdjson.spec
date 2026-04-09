# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           simdjson
Version:        4.2.4
Release:        %autorelease
Summary:        Parsing gigabytes of JSON per second
License:        Apache-2.0 AND MIT
URL:            https://github.com/simdjson/simdjson
#!RemoteAsset:  sha256:6f942d018561a6c30838651a386a17e6e4abbfc396afd0f62740dea1810dedea
Source0:        https://github.com/simdjson/simdjson/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DSIMDJSON_TESTS=ON
BuildOption(conf):  -DSIMDJSON_BUILD_STATIC=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
JSON is everywhere on the Internet. Servers spend a *lot* of time parsing it.
The simdjson library uses commonly available SIMD instructions and microparallel
algorithms to parse JSON extremely fast. This package contains the shared library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The package contains libraries and header files for developing applications
that use %{name}.

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_libdir}/libsimdjson.so.*

%files devel
%doc doc/
%{_includedir}/simdjson.h
%{_libdir}/cmake/simdjson/
%{_libdir}/libsimdjson.so
%{_libdir}/pkgconfig/simdjson.pc

%changelog
%autochangelog
