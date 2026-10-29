# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           simdjson
Version:        5.0.8
Release:        %autorelease
Summary:        Parsing gigabytes of JSON per second
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND BSL-1.0
URL:            https://simdjson.org/
VCS:            git:https://github.com/simdjson/simdjson.git
#!RemoteAsset:  sha256:356cc3a2d6a3d0d45bf5eba813e58ef4f2f6d9cc2a25d8aada2563bc13755789
Source0:        https://github.com/simdjson/simdjson/archive/refs/tags/v%{version}.tar.gz
#!RemoteAsset:  sha256:c9bff75738922193e67fa726fa225535870d2aa1059f91452c411736284ad566
Source1:        https://www.boost.org/LICENSE_1_0.txt
BuildSystem:    cmake

BuildOption(conf):  -DSIMDJSON_TESTS=ON
BuildOption(conf):  -DSIMDJSON_BUILD_STATIC=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(python3)

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

%prep -a
install -m 0644 %{SOURCE1} LICENSE-Boost
sed -n '1,/^\*\//p' src/internal/isadetection.h > LICENSE-BSD

%files
%license LICENSE LICENSE-MIT LICENSE-BSD LICENSE-Boost
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
