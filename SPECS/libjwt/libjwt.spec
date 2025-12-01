# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libjwt
Version:        3.2.2
Release:        %autorelease
Summary:        A Javascript Web Token library in C
License:        MPL-2.0
URL:            https://github.com/benmcollins/libjwt
#!RemoteAsset
Source:         https://github.com/benmcollins/libjwt/releases/download/v%{version}/libjwt-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf): -DBUILD_SHARED_LIBS:BOOL=ON
BuildOption(conf): -DBUILD_STATIC_LIBS:BOOL=OFF
BuildOption(conf): -DBUILD_EXAMPLES:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  jansson-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel

%description
A Javascript Web Token library in C. libjwt provides a simple API for creating,
signing, and verifying JWTs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
This package contains libraries and header files for developing applications
that use the libjwt library.

%install -a
find %{buildroot} -type f -name "*.a" -delete -print

%files
%license LICENSE
%doc %{_docdir}
%doc README.md
%{_libdir}/libjwt.so.*
%{_bindir}/jwk2key
%{_bindir}/jwt-generate
%{_bindir}/jwt-verify
%{_bindir}/key2jwk
%{_mandir}/man1/jwk2key.1*
%{_mandir}/man1/jwt-generate.1*
%{_mandir}/man1/jwt-verify.1*
%{_mandir}/man1/key2jwk.1*

%files devel
%{_includedir}/jwt.h
%{_includedir}/jwt_export.h
%{_libdir}/libjwt.so
%{_libdir}/pkgconfig/libjwt.pc
%{_libdir}/cmake/LibJWT/

%changelog
%{?autochangelog}
