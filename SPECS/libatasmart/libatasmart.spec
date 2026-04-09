# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libatasmart
Version:        0.19
Release:        %autorelease
Summary:        ATA S.M.A.R.T. Disk Health Monitoring Library
License:        LGPL-2.1-or-later
URL:            http://git.0pointer.net/libatasmart
#!RemoteAsset
Source0:        http://0pointer.de/public/libatasmart-%{version}.tar.xz
BuildSystem:    autotools

# Masking high byte, fault tolerance, data truncation.
Patch0:         0001-libatasmart-0.19-wd-fix.patch

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  make
BuildRequires:  vala

%description
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%package        devel
Summary:        Development Files for libatasmart Client Development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Development Files for libatasmart Client Development.

%files
%doc README LGPL
%{_libdir}/libatasmart.so.4*
%{_sbindir}/skdump
%{_sbindir}/sktest

%files devel
%doc blob-examples/*
%{_includedir}/atasmart.h
%{_libdir}/libatasmart.so
%{_libdir}/pkgconfig/libatasmart.pc
%{_datadir}/vala/vapi/atasmart.vapi

%changelog
%autochangelog
