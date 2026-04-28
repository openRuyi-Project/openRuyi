# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtscxml
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtscxml
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - ScXml component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtscxml
#!RemoteAsset:  sha256:eb67a0e5d4c6d488e3013f8dbef859a00e10bb033472eb53688fce350e3a1869
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(openssl)

%description
The Qt SCXML module provides functionality to create state machines from SCXML files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Core)
Requires:       pkgconfig(Qt6Quick)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6Scxml.so.6*
%{_qt6_libdir}/libQt6ScxmlQml.so.6*
%{_qt6_libdir}/libQt6StateMachineQml.so.6*
%{_qt6_libdir}/libQt6StateMachine.so.6*
%{_qt6_libexecdir}/qscxmlc
%{_qt6_qmldir}/QtScxml/
%{_qt6_qmldir}/QtQml/
%dir %{_qt6_pluginsdir}/scxmldatamodel
%{_qt6_pluginsdir}/scxmldatamodel/libqscxmlecmascriptdatamodel.so
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtScxml/
%{_qt6_includedir}/QtScxmlGlobal/
%{_qt6_includedir}/QtScxmlQml/
%{_qt6_includedir}/QtStateMachineQml
%{_qt6_includedir}/QtStateMachine/
%{_qt6_libdir}/libQt6Scxml.so
%{_qt6_libdir}/libQt6Scxml.prl
%{_qt6_libdir}/libQt6ScxmlQml.prl
%{_qt6_libdir}/libQt6ScxmlQml.so
%{_qt6_libdir}/libQt6StateMachine.prl
%{_qt6_libdir}/libQt6StateMachine.so
%{_qt6_libdir}/libQt6StateMachineQml.prl
%{_qt6_libdir}/libQt6StateMachineQml.so
%{_qt6_libdir}/cmake/Qt6Scxml/
%{_qt6_libdir}/cmake/Qt6ScxmlGlobalPrivate/
%{_qt6_libdir}/cmake/Qt6ScxmlPrivate/
%{_qt6_libdir}/cmake/Qt6ScxmlQml/
%{_qt6_libdir}/cmake/Qt6ScxmlQmlPrivate/
%{_qt6_libdir}/cmake/Qt6ScxmlTools/
%{_qt6_libdir}/cmake/Qt6StateMachine/
%{_qt6_libdir}/cmake/Qt6StateMachinePrivate/
%{_qt6_libdir}/cmake/Qt6StateMachineQml/
%{_qt6_libdir}/cmake/Qt6StateMachineQmlPrivate/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtScxmlTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_archdatadir}/mkspecs/features/qscxmlc.prf
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/Qt6Scxml.pc
%{_qt6_libdir}/pkgconfig/Qt6ScxmlQml.pc
%{_qt6_libdir}/pkgconfig/Qt6StateMachine.pc
%{_qt6_libdir}/pkgconfig/Qt6StateMachineQml.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
