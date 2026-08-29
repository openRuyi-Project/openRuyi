# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstream_version 8.1-alpha6
%global os_version 8.1~alpha6

Name:           qhull
Version:        %{os_version}
Release:        %autorelease
Summary:        General dimension convex hull programs
License:        Qhull
URL:            http://www.qhull.org
VCS:            git:https://github.com/qhull/qhull.git
#!RemoteAsset:  sha256:033a155cfed37f811f881d4db16668157027e3cb6c9bf2ac5a036cd44c731dc1
Source0:        https://github.com/qhull/qhull/archive/v%{upstream_version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DLINK_APPS_SHARED=ON

# The static_r library needs fPIC
Patch0:         0001-qhull-staticr-pic.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

%package        libs
Summary:        Rentrant, shared library (libqhull_r.so)

%description    libs
%{summary}

%package        devel
Summary:        Development files for qhull
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

%prep
%autosetup -n %{name}-%{upstream_version} -p1

%files
%license COPYING.txt
%{_pkgdocdir}
%exclude %{_pkgdocdir}/COPYING.txt
%{_bindir}/*
%{_mandir}/man1/*

%files libs
%{_libdir}/libqhull_r.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/*
# Easier to include these than to hack them out of the cmake bits
%{_libdir}/libqhullcpp.a
%{_libdir}/libqhullstatic*.a
%dir %{_libdir}/cmake/Qhull
%{_libdir}/cmake/Qhull/QhullConfig*.cmake
%{_libdir}/cmake/Qhull/QhullTargets*.cmake
%{_libdir}/pkgconfig/qhull_r.pc
%{_libdir}/pkgconfig/qhullcpp.pc
%{_libdir}/pkgconfig/qhullstatic.pc
%{_libdir}/pkgconfig/qhullstatic_r.pc

%changelog
%autochangelog
