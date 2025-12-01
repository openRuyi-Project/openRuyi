# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           duktape
Version:        2.7.0
Release:        %autorelease
Summary:        Embeddable Javascript engine
License:        MIT
URL:            https://duktape.org/
#!RemoteAsset
Source:         https://duktape.org/%name-%{version}.tar.xz
Patch:          0001-duktape-link-m.patch
BuildSystem:    autotools

BuildOption(build):   -f Makefile.sharedlibrary
BuildOption(install): -f Makefile.sharedlibrary INSTALL_PREFIX=%{_prefix}

BuildRequires:  gcc
BuildRequires:  make

%description
Duktape is an embeddable Javascript engine, with a focus on portability and
compact footprint.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
This package contains header files and libraries needed to develop
applications that use %{name}.

%conf -p
sed -i 's@/lib/@/%{_lib}/@g' Makefile.sharedlibrary
sed -i 's@/lib$@/%{_lib}@g' Makefile.sharedlibrary

# No configure
%conf

# no tests
%check

%files
%doc AUTHORS.rst
%license LICENSE.txt
%{_libdir}/libduktape.so.*
%{_libdir}/libduktaped.so.*

%files  devel
%{_includedir}/duk_config.h
%{_includedir}/duktape.h
%{_libdir}/libduktape.so
%{_libdir}/libduktaped.so
%{_libdir}/pkgconfig/duktape.pc

%changelog
%{?autochangelog}
