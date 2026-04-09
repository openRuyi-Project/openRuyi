# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mpdecimal
Version:        4.0.1
Release:        %autorelease
Summary:        Library for general decimal arithmetic
License:        BSD-2-Clause
URL:            https://www.bytereef.org/mpdecimal/index.html
# VCS: No VCS link available
#!RemoteAsset
Source0:        https://www.bytereef.org/software/mpdecimal/releases/mpdecimal-%{version}.tar.gz
#!RemoteAsset
Source1:        https://speleotrove.com/decimal/dectest.zip
BuildSystem:    autotools

BuildOption(conf):  --disable-static
# Set LDXXFLAGS to properly pass the buildroot
# linker flags to the C++ extension.
BuildOption(build):  LDXXFLAGS="%{?build_ldflags}"

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  unzip

%description
The package contains a library libmpdec implementing General Decimal
Arithmetic Specification. The specification, written by Mike Cowlishaw from
IBM, defines a general purpose arbitrary precision data type together with
rigorously specified functions and rounding behavior.

%package     -n %{name}++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Library for general decimal arithmetic (C++)

%description -n %{name}++
The package contains a library libmpdec++ implementing General Decimal
Arithmetic Specification. The specification, written by Mike Cowlishaw from
IBM, defines a general purpose arbitrary precision data type together with
rigorously specified functions and rounding behavior.

%package        devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}++%{?_isa} = %{version}-%{release}
Summary:        Development headers for mpdecimal library

%description    devel
The package contains development headers for the mpdecimal library.

%prep -a
unzip -d tests/testdata %{SOURCE1}

%install -a
# license will go into dedicated directory
rm %{buildroot}%{_docdir}/%{name}/COPYRIGHT.txt

%files
%doc README.txt CHANGELOG.txt
%license COPYRIGHT.txt
%{_libdir}/libmpdec.so.%{version}
%{_libdir}/libmpdec.so.4

%files -n %{name}++
%{_libdir}/libmpdec++.so.%{version}
%{_libdir}/libmpdec++.so.4

%files devel
%{_libdir}/libmpdec.so
%{_libdir}/libmpdec++.so
%{_includedir}/mpdecimal.h
%{_includedir}/decimal.hh
%{_libdir}/pkgconfig/libmpdec.pc
%{_libdir}/pkgconfig/libmpdec++.pc
%{_mandir}/man3/libmpdec.3*
%{_mandir}/man3/libmpdec++.3*
%{_mandir}/man3/mpdecimal*.3*

%changelog
%autochangelog
