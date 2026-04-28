# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtquick3dphysics
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtquick3dphysics
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Quick3D Physics Libraries and utilities
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtquick3dphysics
#!RemoteAsset:  sha256:d973847df1be6ee711e771df923537fb62fcac5bf57100f2ebc6f7742c8d2fee
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  qt6-qtbase-private-devel >= %{version}
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(Qt6ShaderTools) >= %{version}
BuildRequires:  pkgconfig(Qt6Quick3D) >= %{version}

%description
The Qt 6 Quick3D Physics library provides physics simulation capabilities for
Qt Quick 3D.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Gui)
Requires:       pkgconfig(Qt6Quick)
Requires:       pkgconfig(Qt6Quick3D)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6Quick3DPhysics.so.6*
%{_qt6_libdir}/libQt6Quick3DPhysicsHelpers.so.6*
%{_qt6_qmldir}/QtQuick3D/Physics/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_bindir}/cooker
%{_qt6_includedir}/QtQuick3DPhysics/
%{_qt6_includedir}/QtQuick3DPhysicsHelpers/
%{_qt6_libdir}/libQt6BundledPhysX.a
%{_qt6_libdir}/libQt6Quick3DPhysics.so
%{_qt6_libdir}/libQt6Quick3DPhysics.prl
%{_qt6_libdir}/libQt6Quick3DPhysicsHelpers.so
%{_qt6_libdir}/libQt6Quick3DPhysicsHelpers.prl
%{_qt6_libdir}/cmake/Qt6BundledPhysX/
%{_qt6_libdir}/cmake/Qt6Quick3DPhysics/
%{_qt6_libdir}/cmake/Qt6Quick3DPhysicsHelpers/
%{_qt6_libdir}/cmake/Qt6Quick3DPhysicsHelpersPrivate/
%{_qt6_libdir}/cmake/Qt6Quick3DPhysicsPrivate/
%{_qt6_libdir}/cmake/Qt6/FindWrap*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtQuick3DPhysicsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6Quick3DPhysics.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick3DPhysicsHelpers.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
