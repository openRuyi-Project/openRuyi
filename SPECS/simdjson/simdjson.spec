# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global counters_version 3.1.0
%global test_data_commit 351949906abde446f0314bf79606fb5d884f5be7

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
#!RemoteAsset:  sha256:c8cdc32c03816538ce22781ed72964dc864b2a34a310d3b7104812a5ca2d835d
Source2:        https://github.com/cpm-cmake/CPM.cmake/releases/download/v0.40.2/CPM.cmake
#!RemoteAsset:  sha256:cc2bd298d7e48f8b16c648972c9375860c37a20534594d968eee3827b6fe4025
Source3:        https://github.com/lemire/counters/archive/refs/tags/v%{counters_version}.tar.gz
#!RemoteAsset:  sha256:257371accdfca69814ec88841031bd8183409abf5048fff797df516092b6ded9
Source4:        https://github.com/simdjson/simdjson-data/archive/%{test_data_commit}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -G Ninja
BuildOption(conf):  -DSIMDJSON_DEVELOPER_MODE:BOOL=ON
BuildOption(conf):  -DSIMDJSON_ALLOW_DOWNLOADS:BOOL=OFF
BuildOption(conf):  -DCPM_LOCAL_PACKAGES_ONLY:BOOL=ON
BuildOption(conf):  -DCPM_counters_SOURCE:PATH="$PWD/counters-%{counters_version}"
BuildOption(conf):  -DCPM_simdjson-data_SOURCE:PATH="$PWD/simdjson-data-%{test_data_commit}"
BuildOption(check):  --no-tests=error

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
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
%setup -q -T -D -a 3 -a 4
install -m 0644 %{SOURCE2} cmake/CPM.cmake
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
