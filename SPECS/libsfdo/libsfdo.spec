# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsfdo
Version:        0.1.4
Release:        %autorelease
Summary:        Libraries implementing freedesktop.org specifications
License:        BSD-2-Clause
URL:            https://gitlab.freedesktop.org/vyivel/libsfdo
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/vyivel/libsfdo/-/archive/v%{version}/libsfdo-v%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc

%description
libsfdo is a collection of libraries implementing various freedesktop.org
specifications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files needed for developing
applications that use libsfdo.

%files
%license LICENSE
%doc README.md
%{_libdir}/libsfdo-*.so.0

%files devel
%{_includedir}/sfdo-*.h
%{_libdir}/libsfdo-*.so
%{_libdir}/pkgconfig/libsfdo-basedir.pc
%{_libdir}/pkgconfig/libsfdo-desktop-file.pc
%{_libdir}/pkgconfig/libsfdo-desktop.pc
%{_libdir}/pkgconfig/libsfdo-icon.pc

%changelog
%{?autochangelog}
