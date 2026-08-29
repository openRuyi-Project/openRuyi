# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libxcrypt
Version:        4.5.2
Release:        %autorelease
Summary:        Extended crypt library for DES, MD5, Blowfish and others
License:        BSD-2-Clause AND GPL-3.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause AND LicenseRef-openRuyi-Public-Domain
URL:            https://github.com/besser82/libxcrypt
#!RemoteAsset:  sha256:71513a31c01a428bccd5367a32fd95f115d6dac50fb5b60c779d5c7942aec071
Source0:        https://github.com/besser82/libxcrypt/releases/download/v%{version}/libxcrypt-%{version}.tar.xz
BuildSystem:    autotools

# From https://github.com/besser82/libxcrypt/pull/220
Patch0:         fix-werror-discarded-qualifiers.patch

BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --enable-shared
BuildOption(conf):  --enable-static
BuildOption(conf):  --enable-hashes=all
BuildOption(conf):  --with-pkgconfigdir=%{_libdir}/pkgconfig

BuildRequires:  pkgconfig
BuildRequires:  perl

%description
libxcrypt is a modern library for one-way hashing of passwords.
It supports DES, MD5, SHA-2-256, SHA-2-512, and bcrypt-based password
hashes, and provides the traditional Unix 'crypt' and 'crypt_r'
interfaces, as well as a set of extended interfaces pioneered by
Openwall Linux, 'crypt_rn', 'crypt_ra', 'crypt_gensalt',
'crypt_gensalt_rn', and 'crypt_gensalt_ra'.

%package        devel
Summary:        Development files for %{name}
License:        BSD-2-Clause AND LGPL-2.1-or-later AND BSD-3-Clause AND LicenseRef-openRuyi-Public-Domain
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Provides:       glibc-devel:%{_libdir}/libcrypt.so

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static library for -static linking with %{name}
License:        BSD-2-Clause AND GPL-3.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause AND LicenseRef-openRuyi-Public-Domain
Requires:       %{name}-devel = %{version}-%{release}
Requires:       glibc-static
Provides:       glibc-static:%{_libdir}/libcrypt.a

%description    static
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
%{_libdir}/pkgconfig/libcrypt.pc
%{_libdir}/pkgconfig/libxcrypt.pc
%{_mandir}/man?/*

%files static
%{_libdir}/*.a

%changelog
%{?autochangelog}
