# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           olm
Version:        3.2.16
Release:        %autorelease
Summary:        Olm and Megolm cryptographic ratchet library
License:        Apache-2.0 AND BSD-3-Clause AND LicenseRef-openRuyi-Public-Domain
URL:            https://gitlab.matrix.org/matrix-org/olm
#!RemoteAsset:  sha256:1e90f9891009965fd064be747616da46b232086fe270b77605ec9bda34272a68
Source0:        https://gitlab.matrix.org/matrix-org/olm/-/archive/%{version}/olm-%{version}.tar.gz
BuildSystem:    cmake

# Upstream declares CMake 3.4; retain its policy behavior with modern CMake.
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
# Upstream enables CTest only in the tests subdirectory.
BuildOption(check):  --test-dir %{__cmake_builddir}/tests

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Olm implements the Olm and Megolm cryptographic ratchets used by Matrix,
with a C interface for session management, encryption and decryption.

%package        devel
Summary:        Development files for Olm
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, pkg-config metadata and CMake configuration for developing
applications that use the Olm library.

%files
%doc README.md
%license LICENSE
%license lib/crypto-algorithms/README.md
%license lib/curve25519-donna/LICENSE.md
%license lib/ed25519/readme.md
%{_libdir}/libolm.so.*

%files devel
%{_includedir}/olm/
%{_libdir}/cmake/Olm/
%{_libdir}/libolm.so
%{_libdir}/pkgconfig/olm.pc

%changelog
%autochangelog
