# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtwebsockets
%define short_version 6.12

Name:           qt6-qtwebsockets
Version:        6.12.0
Release:        %autorelease
Summary:        Qt6 - WebSockets component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtwebsockets
#!RemoteAsset:  sha256:21690a365cd5fbfa8dea051473e98968df9f4eca0121fed7481d1215b7455a31
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
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(openssl)

%patchlist
# QWebSocket: fix off-by-one header size limit; https://download.qt.io/official_releases/qt/6.12/CVE-2026-114369-qtwebsockets-6.12.zip
1000-qwebsocket-fix-off-by-one-header-size-limit.patch
# QWebSocket: fix quadratic copy and scan during pre-handshake; https://download.qt.io/official_releases/qt/6.12/CVE-2026-114369-qtwebsockets-6.12.zip
1001-qwebsocket-fix-quadratic-copy-and-scan-during-pre-handshake.patch
# QWebSocketServer: Fix quadratic copy and scan during pre-handshake; https://download.qt.io/official_releases/qt/6.12/CVE-2026-114369-qtwebsockets-6.12.zip
1002-qwebsocketserver-fix-quadratic-copy-and-scan-during-pre-handshake.patch
# QWebSocket: fix auth state not being cleared; https://download.qt.io/official_releases/qt/6.12/CVE-2026-114366-qtwebsockets-6.12-0001.diff
1003-qwebsocket-fix-auth-state-not-being-cleared.patch

%description
The QtWebSockets module implements the WebSocket protocol as specified in RFC
6455. It solely depends on Qt (no external dependencies).

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

%install -a
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6WebSockets.so.6*
%{_qt6_qmldir}/QtWebSockets/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx

%files devel
%{_qt6_includedir}/QtWebSockets/
%{_qt6_libdir}/libQt6WebSockets.so
%{_qt6_libdir}/libQt6WebSockets.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWebSocketsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6WebSockets/
%{_qt6_libdir}/cmake/Qt6WebSocketsPrivate/
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_websockets*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6WebSockets.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
