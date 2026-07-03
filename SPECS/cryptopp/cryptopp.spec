# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Sun Yuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname CRYPTOPP_8_9_0

Name:           cryptopp
Version:        8.9.0
Release:        %autorelease
Summary:        Free C++ class library of cryptographic schemes
License:        BSL-1.0 AND LicenseRef-openRuyi-Public-Domain
URL:            https://cryptopp.com/
VCS:            git:https://github.com/weidai11/cryptopp.git
#!RemoteAsset:  sha256:ab5174b9b5c6236588e15a1aa1aaecb6658cdbe09501c7981ac8db276a24d9ab
Source0:        https://github.com/weidai11/cryptopp/archive/refs/tags/%{srcname}.tar.gz#/cryptopp-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -n cryptopp-%{srcname}
BuildOption(build):  shared
BuildOption(build):  libcryptopp.pc
BuildOption(build):  PREFIX=%{_prefix}
BuildOption(build):  LIBDIR=%{_libdir}
BuildOption(build):  CXXFLAGS="%{optflags} -DNDEBUG -fPIC"
BuildOption(build):  LDFLAGS="%{build_ldflags}"

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig

%description
Crypto++ is a free C++ class library of cryptographic schemes. It provides
ciphers, message authentication codes, one-way hash functions, public-key
cryptosystems, key agreement schemes, and more.

%package        devel
Summary:        Development files for cryptopp
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and libraries needed to develop
applications that use the Crypto++ library.

%conf

%install
%make_build install-lib DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} LIBDIR=%{_libdir} \
    LDCONF=/bin/true

# No check
%check

%files
%license License.txt
%{_libdir}/libcryptopp.so.*

%files devel
%doc Readme.txt
%{_includedir}/cryptopp/
%{_libdir}/libcryptopp.so
%{_libdir}/pkgconfig/libcryptopp.pc

%changelog
%autochangelog
