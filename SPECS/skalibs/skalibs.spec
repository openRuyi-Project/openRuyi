# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: avrovadonz2026 <jinyuan.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           skalibs
Version:        2.14.5.1
Release:        %autorelease
Summary:        skarnet.org C library for system programming
License:        ISC
URL:            https://skarnet.org/software/skalibs/
VCS:            git:https://github.com/skarnet/skalibs
#!RemoteAsset:  sha256:fa359c70439b480400a0a2ef68026a2736b315025a9d95df69d34601fb938f0f
Source0:        https://skarnet.org/software/skalibs/skalibs-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-pkgconfig
BuildOption(conf):  --dynlibdir=%{_libdir}
BuildOption(conf):  --pkgconfdir=%{_libdir}/pkgconfig
BuildOption(conf):  --sysdepdir=%{_libdir}/skalibs/sysdeps

BuildRequires:  gcc
BuildRequires:  make

%description
skalibs is the skarnet.org C system programming library. It provides
the libskarnet shared library, development headers and sysdeps metadata
used by software such as mdevd.

%package        devel
Summary:        Development files for skalibs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the headers, pkg-config metadata, static library
and sysdeps data needed to build software against skalibs.

%check
# No upstream test target is provided.

%files
%license COPYING
%doc AUTHORS INSTALL NEWS README README.solaris
%doc doc/*.html
%{_libdir}/libskarnet.so.*

%files devel
%{_includedir}/skalibs/
%{_libdir}/libskarnet.a
%{_libdir}/libskarnet.so
%{_libdir}/pkgconfig/libskarnet.pc
%dir %{_libdir}/skalibs
%dir %{_libdir}/skalibs/sysdeps
%{_libdir}/skalibs/sysdeps/*

%changelog
%{?autochangelog}
