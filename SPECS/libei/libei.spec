# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libei
Version:        1.5.0
Release:        %autorelease
Summary:        Library for Emulated Input
License:        MIT
URL:            http://gitlab.freedesktop.org/libinput/libei
#!RemoteAsset:  sha256:da1fba92daccd0667bc46c3ee952d4ae8cfc6bdb4c0bb4d34df26528fb240618
Source0:        https://gitlab.freedesktop.org/libinput/libei/-/archive/%{version}/libei-%{version}.tar.bz2
BuildSystem:    meson

BuildOption(conf):  -Dtests=disabled
BuildOption(conf):  -Ddocumentation=[]
BuildOption(conf):  -Dliboeffis=enabled

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  libxml2
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  python3-rpm-macros
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(jinja2)

%description
libei is a library to Emulate Input. It allows clients to talk to an EIS
implementatation (Emulated Input Server). This package contains the shared library.

%package        devel
Summary:        Development files for libei
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for libei.

%files
%license COPYING
%{_libdir}/libei.so.1*
%{_libdir}/libeis.so.1*
%{_libdir}/liboeffis.so.1*
%{_bindir}/ei-debug-events

%files devel
%dir %{_includedir}/libei-1.0/
%{_includedir}/libei-1.0/libei.h
%{_libdir}/libei.so
%{_libdir}/pkgconfig/libei-1.0.pc
%{_includedir}/libei-1.0/libeis.h
%{_libdir}/libeis.so
%{_libdir}/pkgconfig/libeis-1.0.pc
%{_includedir}/libei-1.0/liboeffis.h
%{_libdir}/liboeffis.so
%{_libdir}/pkgconfig/liboeffis-1.0.pc

%changelog
%autochangelog
