# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcroco
Summary:        A CSS2 parsing library
Version:        0.6.13
Release:        %autorelease
License:        LGPL-2.0-only
#!RemoteAsset
Source0:        https://download.gnome.org/sources/libcroco/0.6/%{name}-%{version}.tar.xz
BuildSystem:    autotools

# provide pkgconfig
Patch0:         0001-libcroco-0.6.1-multilib.patch
# https://gitlab.gnome.org/GNOME/libcroco/-/merge_requests/5
Patch1:         0002-CVE-2020-12825.patch

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)

%description
CSS2 parsing and manipulation library for GNOME

%package        devel
Summary:        Libraries and include files for developing with libcroco
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides the necessary development libraries and include
files to allow you to develop with libcroco.

%files
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README
%{_bindir}/csslint-0.6
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/libcroco-0.6
%{_bindir}/croco-0.6-config
%{_libdir}/pkgconfig/libcroco-0.6.pc
%{_datadir}/gtk-doc/html/libcroco

%changelog
%autochangelog
