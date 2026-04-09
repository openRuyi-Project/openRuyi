# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtlanguageserver
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtlanguageserver
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - LanguageServer component
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtlanguageserver
#!RemoteAsset
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  qt6-qtbase-private-devel

%description
The Qt Language Server component provides an implementation of the Language
Server protocol.

%package        devel
Summary:        Development files for %{name}

%description    devel
Development files for %{name}.

%files devel
%license LICENSES/*
%{_qt6_includedir}/QtJsonRpc/
%{_qt6_includedir}/QtLanguageServer/
%{_qt6_libdir}/libQt6JsonRpc.a
%{_qt6_libdir}/libQt6JsonRpc.prl
%{_qt6_libdir}/libQt6LanguageServer.a
%{_qt6_libdir}/libQt6LanguageServer.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtLanguageServer*
%{_qt6_libdir}/cmake/Qt6JsonRpcPrivate/
%{_qt6_libdir}/cmake/Qt6LanguageServerPrivate/
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_jsonrpc*.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_languageserver*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/JsonRpcPrivate.json
%{_qt6_datadir}/modules/LanguageServerPrivate.json
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%changelog
%autochangelog
