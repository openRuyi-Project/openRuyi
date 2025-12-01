# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lksctp-tools
Version:        1.0.21
Release:        %autorelease
Summary:        Linux Kernel Stream Control Transmission Protocol Tools
License:        GPL-2.0-or-later AND LGPL-2.0-only AND MIT
URL:            https://github.com/sctp/lksctp-tools/wiki
#!RemoteAsset
Source0:        https://github.com/sctp/lksctp-tools/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:    autotools
BuildOption(conf): --disable-static

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake

%description
This is the lksctp-tools package for Linux Kernel SCTP (Stream Control
Transmission Protocol) Reference Implementation.

This package is intended to supplement the Linux Kernel SCTP Reference
Implementation now available in the Linux kernel source tree in
versions 2.5.36 and following. For more information on LKSCTP see the
package documentation README file, section titled "LKSCTP - Linux
Kernel SCTP."

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for %{name} which include header files and dynamic
libraries.

%conf -p
rm -rf configure && sh bootstrap

%conf -a
# remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%files
%defattr(-,root,root)
%license COPYING*
%doc AUTHORS ChangeLog README doc/*.txt
%{_bindir}/*
%{_libdir}/libsctp.so.*
%{_libdir}/lksctp-tools/libwithsctp.so.*
%{_mandir}/man7/*

%files devel
%{_includedir}/*
%{_libdir}/libsctp.so
%{_libdir}/lksctp-tools/libwithsctp.so
%{_datadir}/lksctp-tools/
%{_libdir}/pkgconfig/libsctp.pc
%{_mandir}/man3/*

%changelog
%{?autochangelog}
