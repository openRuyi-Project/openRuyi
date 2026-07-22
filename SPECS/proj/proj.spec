# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           proj
Version:        9.8.1
Release:        %autorelease
Summary:        Cartographic projection and coordinate transformation library
License:        MIT
URL:            https://proj.org/
VCS:            git:https://github.com/OSGeo/PROJ.git
#!RemoteAsset:  sha256:af5b731c145c1d13c4e3b4eeb7d167e94e845e440f71e3496b4ed8dae0291960
Source0:        https://download.osgeo.org/proj/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(sqlite3)

%description
PROJ transforms geospatial coordinates between coordinate reference systems.

%package        devel
Summary:        Development files for PROJ
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, libraries, and CMake files for developing applications with PROJ.

%install -a
rm -rf %{buildroot}%{_docdir}/%{name}

%files
%doc AUTHORS.md
%doc NEWS.md
%doc README.md
%license COPYING
%{_bindir}/cct
%{_bindir}/cs2cs
%{_bindir}/geod
%{_bindir}/gie
%{_bindir}/invgeod
%{_bindir}/invproj
%{_bindir}/proj
%{_bindir}/projinfo
%{_bindir}/projsync
%{_datadir}/bash-completion/completions/projinfo
%{_datadir}/proj/
%{_libdir}/libproj.so.*
%{_mandir}/man1/*

%files devel
%{_includedir}/*
%{_libdir}/cmake/proj/
%{_libdir}/cmake/proj4/
%{_libdir}/libproj.so
%{_libdir}/pkgconfig/proj.pc

%changelog
%autochangelog
