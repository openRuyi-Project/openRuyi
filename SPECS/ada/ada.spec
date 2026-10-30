# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ada
Version:        4.0.0
Release:        %autorelease
Summary:        WHATWG URL parser
License:        Apache-2.0 OR MIT
URL:            https://ada-url.com/
VCS:            git:https://github.com/ada-url/ada
#!RemoteAsset:  sha256:6d6c7ef7dd2e329320d34eb2ab29ccdc879ee3935af9dfb894a6640e58dc381d
Source0:        https://github.com/ada-url/ada/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

# Use the system simdjson package; https://src.fedoraproject.org/rpms/ada-url/blob/2d879cf10d96d3b8c1ddd792efdedf37bf5ad1e2/f/1000-Remove-cmake-CPM.patch.
Patch2000:      2000-use-system-simdjson.patch

BuildOption(conf):  -DADA_TESTING:BOOL=OFF
BuildOption(check):  --test-dir test-build

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(simdjson)

%description
Ada parses and normalizes URLs according to the WHATWG URL Standard.
It provides C and C++ interfaces and supports URL patterns.

%package        devel
Summary:        Development files for Ada
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and build metadata for applications that use Ada.

%check -p
# Keep the test-only regex provider out of the installed library.
%cmake -B test-build -DADA_TESTING:BOOL=ON \
    -DCPM_LOCAL_PACKAGES_ONLY:BOOL=ON \
    -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON
%{__cmake} --build test-build --parallel %{_smp_build_ncpus}

%files
%doc README.md
%license LICENSE-APACHE LICENSE-MIT
%{_libdir}/libada.so.4
%{_libdir}/libada.so.4.*

%files devel
%{_includedir}/ada.h
%{_includedir}/ada_c.h
%{_includedir}/ada/
%{_libdir}/libada.so
%{_libdir}/cmake/ada/
%{_libdir}/pkgconfig/ada.pc

%changelog
%autochangelog
