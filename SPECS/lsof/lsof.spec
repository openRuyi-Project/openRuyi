# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:          lsof
Version:       4.99.5
Release:       %autorelease
Summary:       A tool for listing open files
License:       Sendmail and LGPL-2.1-or-later and Zlib
URL:           https://lsof.readthedocs.io/en/latest/
#!RemoteAsset
Source0:       https://github.com/lsof-org/lsof/releases/download/%{version}/lsof-%{version}.tar.gz

BuildSystem:    autotools

BuildOption(conf): --disable-static
BuildOption(conf): --enable-security
BuildOption(conf): --enable-no-sock-security

BuildRequires: gcc make
BuildRequires: pkgconfig(libtirpc)
BuildRequires: libselinux-devel
BuildRequires: groff

%description
lsof is a Unix administrative tool that displays information about files
open to processes. It runs on many Unix dialects.

%package devel
Summary:        Development files for the lsof library
Requires:       %{name} = %{version}

%description    devel
This package contains the header files and development library for lsof.

%build -a
soelim -r Lsof.8 > lsof.1

%install -a
install -m 0644 lsof.1 -D %{buildroot}%{_mandir}/man1/lsof.1
rm -rf %{buildroot}%{_mandir}/man8/lsof.8*

%files
%license COPYING
%doc 00CREDITS 00README 00FAQ 00LSOF-L 00QUICKSTART
%{_bindir}/lsof
%{_libdir}/liblsof.so.*
%{_mandir}/man1/lsof.1*

%files devel
%{_libdir}/liblsof.so
%{_includedir}/*.h

%changelog
%{?autochangelog}
