# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsodium
Version:        1.0.20
Release:        %autorelease
Summary:        Portable NaCl-based crypto library
License:        ISC
URL:            https://github.com/jedisct1/libsodium
#!RemoteAsset
Source:         https://download.libsodium.org/libsodium/releases/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --disable-static
BuildOption(conf): --disable-silent-rules

BuildRequires:  gcc

%description
Sodium is a portable, cross-compilable, installable, packageable fork of NaCl,
a new easy-to-use high-speed software library for network communication,
encryption, decryption, signatures, etc.

%package devel
Summary:        Development files for the libsodium crypto library
Requires:       %{name} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libsodium.


%install -a
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license LICENSE
%{_libdir}/%{name}.so.26*

%files devel
%doc AUTHORS ChangeLog README.markdown THANKS
%{_includedir}/sodium.h
%{_includedir}/sodium
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%{?autochangelog}
