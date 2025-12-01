# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:          jitterentropy
Version:       3.6.3
Release:       %autorelease
Summary:       A library for hardware RNG based on CPU timing jitter
License:       BSD-3-Clause OR GPL-2.0-only
URL:           https://www.chronox.de/jent/
#!RemoteAsset
Source0:       https://www.chronox.de/jent/releases/%{version}/%{name}-library-%{version}.tar.xz

BuildSystem:   autotools

BuildOption(build):     LDFLAGS="-lpthread"
BuildOption(install):   PREFIX=%{_prefix}
BuildOption(install):   LIBDIR=%{_lib}

BuildRequires:  gcc
BuildRequires:  make

%description
The Jitter RNG provides a noise source using the CPU execution timing jitter.
This package contains the runtime shared library needed by applications.

%package devel
Summary:       Development files for the jitterentropy library
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, development symlinks, and static
library for compiling applications that use the jitterentropy library.

%conf
# No configure

%build -p
sed -e '/\tgzip .*\/man\// d' -i Makefile
sed -e 's/$(INSTALL_STRIP)/install/' -i Makefile

# no tests
%check

%files
%license LICENSE LICENSE.bsd LICENSE.gplv2
%doc README.md
%{_libdir}/libjitterentropy.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/libjitterentropy.so
%{_mandir}/man3/*

%changelog
%{?autochangelog}
