# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define rname kwindowsystem
%define qt6_version 6.8.0

Name:           kf6-kwindowsystem
Version:        6.28.0
Release:        %autorelease
Summary:        KDE Access to window manager
License:        LGPL-2.1-or-later
URL:            https://kde.org
VCS:            git:https://invent.kde.org/frameworks/kwindowsystem
#!RemoteAsset:  sha256:5adbdf9c82b1ecbb92bda6498ea1b8f88c08f9ec57dbff70d582e2453bf16b12
Source0:        https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  xz
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  xmlto
BuildRequires:  pkgconfig
BuildRequires:  kf6-extra-cmake-modules >= 6.28.0
BuildRequires:  qt6-qtbase-private-devel >= 6.8.0
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(wayland-protocols) >= 1.21.0
BuildRequires:  plasma-wayland-protocols
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  xcb-util
BuildRequires:  libxml2
BuildRequires:  libxslt

%description
Convenience access to certain properties and features of the window manager.

KWindowSystem provides information about the state of the window manager and
allows asking the window manager to change the using a more high-level
interface than the NETWinInfo/NETRootInfo low-level classes.

%package        devel
Summary:        KDE Access to window manager: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Gui) >= 6.8.0
Requires:       xcb-util
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcb)

%description    devel
Convenience access to certain properties and features of the window manager.

KWindowSystem provides information about the state of the window manager and
allows asking the window manager to change the using a more high-level
interface than the NETWinInfo/NETRootInfo low-level classes.
Development files.

%files
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kwindowsystem.categories
%{_kf6_debugdir}/kwindowsystem.renamecategories
%dir %{_kf6_plugindir}/kf6/kwindowsystem
%{_kf6_plugindir}/kf6/kwindowsystem/KF6WindowSystemKWaylandPlugin.so
%{_kf6_plugindir}/kf6/kwindowsystem/KF6WindowSystemX11Plugin.so
%{_kf6_libdir}/libKF6WindowSystem.so.*
%{_datadir}/locale/*/LC_MESSAGES/kwindowsystem6_qt.qm
%{_kf6_qmldir}/org/kde/kwindowsystem/

%files devel
%{_kf6_includedir}/KWindowSystem/
%{_kf6_cmakedir}/KF6WindowSystem/
%{_kf6_libdir}/libKF6WindowSystem.so
%{_kf6_pkgconfigdir}/KF6WindowSystem.pc

%changelog
%autochangelog
