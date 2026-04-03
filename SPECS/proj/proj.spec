# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: lunaticlegacy <baoyi.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           proj
Version:        9.5.1
Release:        %autorelease
Summary:        Cartographic projections and coordinate transformations
License:        MIT
URL:            https://proj.org/
VCS:            git:https://github.com/OSGeo/PROJ.git
#!RemoteAsset
Source0:        https://github.com/OSGeo/PROJ/releases/download/%{version}/proj-%{version}.tar.gz
BuildSystem:    cmake

# Build options for cmake
BuildOption(conf):  -DBUILD_SHARED_LIBS=ON

BuildRequires:  cmake
BuildRequires:  pkgconfig(sqlite)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libcurl)

%description
PROJ is a generic coordinate transformation software that transforms
geospatial coordinates from one coordinate reference system (CRS) to
another.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files, development libraries, and pkg-config files for developing
applications against %{name}.

%files
%doc COPYING
%doc README.md AUTHORS.md NEWS.md
%{_bindir}/proj
%{_bindir}/invproj
%{_bindir}/cs2cs
%{_bindir}/geod
%{_bindir}/invgeod
%{_bindir}/cct
%{_bindir}/gie
%{_bindir}/projinfo
%{_bindir}/projsync
%{_libdir}/libproj.so.*
%{_datadir}/proj/

%files devel
%{_includedir}/geodesic.h
%{_includedir}/proj.h
%{_includedir}/proj_constants.h
%{_includedir}/proj_experimental.h
%{_includedir}/proj_symbol_rename.h
%{_includedir}/proj/
%{_libdir}/libproj.so
%{_libdir}/cmake/proj/
%{_libdir}/cmake/proj4/
%{_libdir}/pkgconfig/proj.pc

%changelog
%{?autochangelog}
