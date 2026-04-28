# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtremoteobjects
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtremoteobjects
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Qt Remote Objects
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtremoteobjects
#!RemoteAsset:  sha256:7c9e56dbe2c400e33d13626a27d822a7c95b7d95f2272b198a788c2b4a9b8a0d
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
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0

%description
Qt Remote Objects (QtRO) is an inter-process communication (IPC) module
developed for Qt.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Gui)
Requires:       pkgconfig(Qt6Network)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/*
%{_qt6_libexecdir}/repc
%{_qt6_libdir}/libQt6RemoteObjects.so.6*
%{_qt6_libdir}/libQt6RemoteObjectsQml.so.6*
%{_qt6_qmldir}/QtRemoteObjects/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtRemoteObjects/
%{_qt6_includedir}/QtRepParser/
%{_qt6_includedir}/QtRemoteObjectsQml/
%{_qt6_libdir}/libQt6RemoteObjects.so
%{_qt6_libdir}/libQt6RemoteObjects.prl
%{_qt6_libdir}/libQt6RemoteObjectsQml.prl
%{_qt6_libdir}/libQt6RemoteObjectsQml.so
%{_qt6_libdir}/cmake/Qt6RemoteObjects/
%{_qt6_libdir}/cmake/Qt6RemoteObjectsPrivate/
%{_qt6_libdir}/cmake/Qt6RemoteObjectsQml/
%{_qt6_libdir}/cmake/Qt6RemoteObjectsQmlPrivate/
%{_qt6_libdir}/cmake/Qt6RemoteObjectsTools/
%{_qt6_libdir}/cmake/Qt6RepParser/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtRemoteObjectsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_archdatadir}/mkspecs/features/*
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6RemoteObjects.pc
%{_qt6_libdir}/pkgconfig/Qt6RemoteObjectsQml.pc
%{_qt6_libdir}/pkgconfig/Qt6RepParser.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
