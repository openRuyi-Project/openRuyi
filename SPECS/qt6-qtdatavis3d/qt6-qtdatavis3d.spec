# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtdatavis3d
%define short_version 6.12

Name:           qt6-qtdatavis3d
Version:        6.12.0
Release:        %autorelease
Summary:        Qt6 - Qt Data Visualization component
License:        GPL-3.0-only AND BSD-3-Clause
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtdatavis3d
#!RemoteAsset:  sha256:5f79b948eb1e81ff7f69e335b075c1b48953d88f5d97970b537e348dbbaa98dc
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -GNinja
BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(openssl)

%description
Qt Data Visualization module provides multiple graph types to visualize data in
3D space both with C++ and Qt Quick 2.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6OpenGL)
Requires:       pkgconfig(Qt6Gui)
Requires:       pkgconfig(Qt6Quick)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/GPL*
%{_qt6_libdir}/libQt6DataVisualization.so.6*
%{_qt6_libdir}/libQt6DataVisualizationQml.so.6*
%{_qt6_qmldir}/QtDataVisualization/
%{_qt6_archdatadir}/sbom/qtdatavisualization-%{version}.spdx

%files devel
%{_qt6_includedir}/QtDataVisualization/
%{_qt6_includedir}/QtDataVisualizationQml/
%{_qt6_libdir}/libQt6DataVisualization.so
%{_qt6_libdir}/libQt6DataVisualization.prl
%{_qt6_libdir}/libQt6DataVisualizationQml.prl
%{_qt6_libdir}/libQt6DataVisualizationQml.so
%{_qt6_libdir}/cmake/Qt6DataVisualization/
%{_qt6_libdir}/cmake/Qt6DataVisualizationPrivate/
%{_qt6_libdir}/cmake/Qt6DataVisualizationQml/
%{_qt6_libdir}/cmake/Qt6DataVisualizationQmlPrivate/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtDataVisualizationTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/Qt6DataVisualization.pc
%{_qt6_libdir}/pkgconfig/Qt6DataVisualizationQml.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
