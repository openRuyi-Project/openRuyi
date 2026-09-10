# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: lunaticlegacy <baoyi.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           geos
Version:        3.13.0
Release:        %autorelease
Summary:        Geometry Engine, Open Source
License:        LGPL-2.1-or-later
URL:            https://libgeos.org/
VCS:            git:https://github.com/libgeos/geos.git
#!RemoteAsset
Source:         https://github.com/libgeos/geos/releases/download/%{version}/geos-%{version}.tar.bz2
BuildSystem:    cmake

# Skip failing test on RISC-V due to floating point precision differences
# https://github.com/libgeos/geos/issues/947
Patch0:         0001-skip-riscv-floating-point-test.patch

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON

BuildRequires:  cmake

%description
GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology
Suite (JTS). It includes the OpenGIS Simple Features for SQL spatial
predicate functions and spatial operators.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files, development libraries, and pkg-config files for developing
applications against %{name}.

%files
%license COPYING
%doc README.md
%doc NEWS.md
%doc Version.txt
%doc AUTHORS
%{_bindir}/geosop
%{_libdir}/libgeos.so.*
%{_libdir}/libgeos_c.so.*

%files          devel
%{_bindir}/geos-config
%{_includedir}/geos.h
%{_includedir}/geos_c.h
%{_includedir}/geos/
%dir %{_libdir}/cmake/GEOS
%{_libdir}/libgeos.so
%{_libdir}/libgeos_c.so
%{_libdir}/pkgconfig/geos.pc
%{_libdir}/cmake/GEOS/*.cmake

%changelog
%autochangelog