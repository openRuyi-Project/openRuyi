# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           qcoro
Version:        0.12.0
Release:        %autorelease
Summary:        C++ Coroutines for Qt 6
License:        MIT
URL:            https://github.com/danvratil/qcoro
#!RemoteAsset:  sha256:809afafab61593f994c005ca6e242300e1e3e7f4db8b5d41f8c642aab9450fbc
Source0:        https://github.com/qcoro/qcoro/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_BUILD_TYPE=Release
BuildOption(conf):  -DUSE_QT_VERSION:STRING=6
BuildOption(conf):  -DECM_MKSPECS_INSTALL_DIR=%{_libdir}/qt6/mkspecs/modules
BuildOption(conf):  -DQCORO_BUILD_EXAMPLES:BOOL=OFF
BuildOption(conf):  -DQCORO_ENABLE_ASAN:BOOL=OFF
BuildOption(conf):  -DQCORO_WITH_QML:BOOL=ON
BuildOption(conf):  -DQCORO_WITH_QTDBUS:BOOL=ON
BuildOption(conf):  -DQCORO_WITH_QTNETWORK:BOOL=ON
BuildOption(conf):  -DQCORO_WITH_QTQUICK:BOOL=ON
BuildOption(conf):  -DQCORO_WITH_QTWEBSOCKETS:BOOL=ON
BuildOption(conf):  -DBUILD_TESTING:BOOL=ON
BuildOption(check):  --timeout 3600 -E "networkreply|test-qdbus"

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-private-devel

%description
The QCoro library provides set of tools to make use of the C++20 coroutines
in connection with certain asynchronous Qt actions.

%package        devel
Summary:        Development files for QCoro (Qt 6 version)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel

%description    devel
Development files for QCoro (Qt 6).

%files
%doc README.md
%license LICENSES/*
%{_libdir}/libQCoro6*.so.*

%files devel
%{_includedir}/qcoro6/
%{_libdir}/cmake/QCoro6*/
%{_libdir}/libQCoro6*.so
%{_libdir}/qt6/mkspecs/modules/qt_QCoro*.pri

%changelog
%autochangelog
