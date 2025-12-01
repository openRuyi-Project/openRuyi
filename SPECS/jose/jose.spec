# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jose
Version:        14
Release:        %autorelease
Summary:        A C-language implementation of Javascript Object Signing and Encryption
License:        Apache-2.0
URL:            https://github.com/latchset/jose
#!RemoteAsset
Source0:        https://github.com/latchset/jose/releases/download/v%{version}/jose-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf): -Ddocs=disabled

BuildRequires:  gcc meson ninja
BuildRequires:  jansson-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
José is a C-language implementation of the Javascript Object Signing and
Encryption (JOSE) standards. It provides a command-line utility which
encompasses most of the JOSE features, allowing for easy integration into
projects and one-off scripts.

%package devel
Summary:        Development libraries and files for libjose
Requires:       %{name} = %{version}
Requires:       pkgconfig(jansson)

%description devel
This package contains the libraries, header files, and documentation for
developing applications that use the José library.


%install -a
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_licensedir}/%{name}/COPYING

%files
%license COPYING
%{_bindir}/jose
%{_libdir}/libjose.so.*

%files devel
%doc COPYING
%dir %{_includedir}/jose
%{_includedir}/jose/*.h
%{_libdir}/libjose.so
%{_libdir}/pkgconfig/jose.pc
%{_mandir}/man3/jose*.3*

%changelog
%{?autochangelog}
