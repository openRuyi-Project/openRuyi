# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qthttpserver
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qthttpserver
Version:        6.10.1
Release:        %autorelease
Summary:        Library to facilitate the creation of an http server with Qt
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qthttpserver
#!RemoteAsset
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
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6WebSockets) >= %{version}
BuildRequires:  pkgconfig(xkbcommon)

%description
Library to facilitate the creation of an http server with Qt.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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
%{_qt6_libdir}/libQt6HttpServer.so.6*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtHttpServer/
%{_qt6_libdir}/libQt6HttpServer.so
%{_qt6_libdir}/libQt6HttpServer.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtHttpServerTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6HttpServer/
%{_qt6_libdir}/cmake/Qt6HttpServerPrivate/
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6HttpServer.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
