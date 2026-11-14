# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           box2d
Version:        3.2.0
Release:        %autorelease
Summary:        Two-dimensional rigid body physics engine
License:        MIT
URL:            https://github.com/erincatto/box2d
#!RemoteAsset:  sha256:ffec747b27a2267016f8d0240d658c82d187fb2271fa0f69fcbe53fbc067180d
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DBOX2D_SAMPLES=OFF
BuildOption(conf):  -DBOX2D_UNIT_TESTS=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Box2D simulates motion, contacts and constraints in two dimensions.
It provides a C interface for constructing and stepping a physics world.

%package        devel
Summary:        Development files for Box2D
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and build metadata for developing with Box2D.

%files
%doc README.md
%license LICENSE
%{_libdir}/libbox2d.so.*

%files devel
%{_includedir}/box2d/
%{_libdir}/cmake/box2d/
%{_libdir}/libbox2d.so
%{_libdir}/pkgconfig/box2d.pc

%changelog
%autochangelog
