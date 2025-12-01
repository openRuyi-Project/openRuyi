# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libxcrypt
Version:        4.4.38
Release:        %autorelease
Summary:        Extended crypt library for DES, MD5, Blowfish and others
License:        BSD-2-Clause AND GPL-3.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause AND Public-Domain
URL:            https://github.com/besser82/libxcrypt
#!RemoteAsset
Source0:        https://github.com/besser82/libxcrypt/releases/download/v%{version}/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://github.com/besser82/libxcrypt/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
#!RemoteAsset
Source2:        https://github.com/besser82/libxcrypt/releases/download/v%{version}/libxcrypt-gpgkey.asc#/%{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  perl
BuildSystem:    autotools
BuildOption(conf): --disable-silent-rules
BuildOption(conf): --enable-shared
BuildOption(conf): --enable-static
BuildOption(conf): --enable-hashes=all
BuildOption(conf): --with-pkgconfigdir=%{_libdir}/pkgconfig

%description
libxcrypt is a modern library for one-way hashing of passwords.
It supports DES, MD5, SHA-2-256, SHA-2-512, and bcrypt-based password
hashes, and provides the traditional Unix 'crypt' and 'crypt_r'
interfaces, as well as a set of extended interfaces pioneered by
Openwall Linux, 'crypt_rn', 'crypt_ra', 'crypt_gensalt',
'crypt_gensalt_rn', and 'crypt_gensalt_ra'.

%package devel
Summary:        Development files for %{name}
License:        BSD-2-Clause AND LGPL-2.1-or-later AND BSD-3-Clause AND Public-Domain
Requires:       %{name} = %{version}
Requires:       pkgconfig >= 0.9.0
Conflicts:      glibc-devel < 2.28
Provides:       glibc-devel:%{_libdir}/libcrypt.so

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package static
Summary:        Static library for -static linking with %{name}
License:        BSD-2-Clause AND GPL-3.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause AND Public-Domain
Requires:       %{name}-devel = %{version}
Requires:       glibc-static
Conflicts:      glibc-static < 2.28
Provides:       glibc-static:%{_libdir}/libcrypt.a

%description static
This package contains the libxcrypt static libraries for -static
linking.  You don't need this, unless you link statically, which
is highly discouraged.

%files
%license COPYING.LIB LICENSING
%doc AUTHORS NEWS THANKS
%{_libdir}/*.so.*

%files devel
%doc TODO
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man?/*

%files static
%{_libdir}/*.a

%changelog
%{?autochangelog}
