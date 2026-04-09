# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           layer-shell-qt
Version:        6.5.91
Release:        %autorelease
Summary:        Library to easily use clients based on wlr-layer-shell
License:        BSD-3-Clause AND CC0-1.0 AND LGPL-3.0-or-later AND MIT
URL:            https://invent.kde.org/plasma/layer-shell-qt
#!RemoteAsset:  sha256:57a4812334e330d995011b21395eae55113a1a40f02e7fb905105a098c769d4e
Source0:        https://download.kde.org/unstable/plasma/%{version}/layer-shell-qt-%{version}.tar.xz
BuildSystem:    cmake

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  pkgconfig(Qt6WaylandCompositor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  wayland-protocols
BuildRequires:  pkgconfig(xkbcommon)

%description
This component is meant for applications to be able to easily use clients
based on wlr-layer-shell protocol.

%package        devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Core)

%description    devel
Developer files for layer-shell-qt.

%files
%license LICENSES/*
%{_libdir}/libLayerShellQtInterface.so.*
%{_qt6_pluginsdir}/wayland-shell-integration/liblayer-shell.so
%{_qt6_qmldir}/org/kde/layershell/

%files devel
%{_includedir}/LayerShellQt/
%{_libdir}/libLayerShellQtInterface.so
%{_libdir}/cmake/LayerShellQt/

%changelog
%autochangelog
