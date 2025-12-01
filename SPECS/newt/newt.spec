# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:         newt
Version:      0.52.25
Release:      %autorelease
Summary:      A library for text mode user interfaces
License:      LGPL-2.0-only
URL:          https://pagure.io/newt
#!RemoteAsset
Source:       https://pagure.io/releases/newt/newt-%{version}.tar.gz

BuildSystem:    autotools
BuildOption(conf):  --without-python
BuildOption(conf):  --without-tcl
BuildOption(conf):  --enable-shared

BuildRequires:  gcc
BuildRequires:  popt-devel
BuildRequires:  slang-devel
BuildRequires:  make
BuildRequires:  pkgconfig

%description
Newt is a programming library for color text-mode, widget-based user
interfaces.

%package      devel
Summary:      Development files for %{name}
Requires:     %{name} = %{version}
Requires:     slang-devel

%description    devel
This package contains the header files and development libraries
needed to build applications that use the newt library.


%install -a
find %{buildroot} -type f -name "*.la" -delete

rm -rf %{buildroot}%{_datadir}/locale

%files
%license COPYING
%doc AUTHORS README CHANGES peanuts.py popcorn.py
%{_bindir}/whiptail
%{_libdir}/libnewt.so.*
%{_mandir}/man1/whiptail.1*

%files devel
%{_includedir}/newt.h
%{_libdir}/libnewt.so
%{_libdir}/pkgconfig/libnewt.pc
%{_libdir}/libnewt.a

%changelog
%{?autochangelog}
