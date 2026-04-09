# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtwebview
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtwebview
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - WebView component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtwebview
#!RemoteAsset
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickPrivate)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineCorePrivate)
BuildRequires:  cmake(Qt6WebEngineQuick)
BuildRequires:  cmake(Qt6WebEngineQuickPrivate)
BuildRequires:  pkgconfig(xkbcommon)

%description
Qt WebView provides a way to display web content in a QML application
without necessarily including a full web browser stack by using native
APIs where it makes sense.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Gui)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/GPL* LICENSES/LGPL*
%{_qt6_libdir}/libQt6WebView.so.6*
%{_qt6_libdir}/libQt6WebViewQuick.so.6*
%{_qt6_qmldir}/QtWebView/
%dir %{_qt6_pluginsdir}/webview/
%{_qt6_pluginsdir}/webview/libqtwebview_webengine.so
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtWebView/
%{_qt6_includedir}/QtWebViewQuick/
%{_qt6_libdir}/cmake/Qt6WebView/
%{_qt6_libdir}/cmake/Qt6WebViewPrivate/
%{_qt6_libdir}/cmake/Qt6WebViewQuick/
%{_qt6_libdir}/cmake/Qt6WebViewQuickPrivate/
%{_qt6_libdir}/cmake/Qt6/FindWebView2.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWebViewTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/libQt6WebView.so
%{_qt6_libdir}/libQt6WebView.prl
%{_qt6_libdir}/libQt6WebViewQuick.so
%{_qt6_libdir}/libQt6WebViewQuick.prl
%{_qt6_libdir}/pkgconfig/Qt6WebView.pc
%{_qt6_libdir}/pkgconfig/Qt6WebViewQuick.pc
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/*.json
%{_qt6_datadir}/modules/*.json

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
