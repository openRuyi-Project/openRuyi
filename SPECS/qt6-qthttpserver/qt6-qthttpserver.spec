# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qthttpserver
%define short_version 6.12

Name:           qt6-qthttpserver
Version:        6.12.0
Release:        %autorelease
Summary:        Library to facilitate the creation of an http server with Qt
License:        GPL-3.0-only AND BSD-3-Clause
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qthttpserver
#!RemoteAsset:  sha256:ede040264551d0930ea5f6c1a4c18a7a3dea59d635e71cd2e81f02567d7814a4
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
BuildSystem:    cmake

# Cap chunk-size line length to prevent memory exhaustion; https://download.qt.io/official_releases/qt/6.12/CVE-2026-110944-qthttpserver-6.12-0001.diff
Patch0:         1000-cap-chunk-size-line-length-to-prevent-memory-exhaustion.patch
# Validate chunk size and reject malformed or out-of-range values; https://download.qt.io/official_releases/qt/6.12/CVE-2026-110944-qthttpserver-6.12-0002.diff
Patch1:         1001-validate-chunk-size-and-reject-malformed-or-out-of-range-values.patch

BuildOption(conf):  -GNinja
BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  ninja
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
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx

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
