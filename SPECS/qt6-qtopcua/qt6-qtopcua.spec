# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtopcua
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtopcua
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - OPC UA component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtopcua
#!RemoteAsset:  sha256:15b70b358d7ffefe8693539505c8ef5b03641d3744d1d3ef728f6646119d0d58
Source0:        https://github.com/qt/%{qt_module}/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(openssl)

%description
Qt OPC UA (API) provides classes and functions to access the OPC UA protocol.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Network)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6OpcUa.so.*
%{_qt6_pluginsdir}/opcua/libopen62541_backend.so
%{_qt6_libdir}/libQt6DeclarativeOpcua.so.*
%{_qt6_qmldir}/QtOpcUa/
%{_qt6_bindir}/qopcuaxmldatatypes2cpp
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtOpcUa/
%{_qt6_includedir}/QtDeclarativeOpcua/
%{_qt6_libdir}/libQt6OpcUa.so
%{_qt6_libdir}/libQt6OpcUa.prl
%{_qt6_libdir}/libQt6DeclarativeOpcua.so
%{_qt6_libdir}/libQt6DeclarativeOpcua.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtOpcUaTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6OpcUa/
%{_qt6_libdir}/cmake/Qt6DeclarativeOpcua/
%{_qt6_libdir}/cmake/Qt6DeclarativeOpcuaPrivate/
%{_qt6_libdir}/cmake/Qt6OpcUaPrivate/
%{_qt6_libdir}/cmake/Qt6OpcUaTools/
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6DeclarativeOpcua.pc
%{_qt6_libdir}/pkgconfig/Qt6OpcUa.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
