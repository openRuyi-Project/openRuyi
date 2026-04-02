# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kidletime
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kidletime
Version:        6.22.0
Release:        %autorelease
Summary:        User and system idle time reporting singleton
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kidletime.git
#!RemoteAsset:  sha256:0701ba4c321785ba670f4a9dba54c551ffd476451caba2c77b9f079e8db42a2e
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(wayland-protocols) >= 1.27
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)

%description
KIdleTime is a singleton reporting information on idle time. It is useful not
only for finding out about the current idle time of the PC, but also for getting
notified upon idle time events, such as custom timeouts, or user activity.

%package        plugins
Summary:        User and system idle time reporting singleton

%description    plugins
KIdleTime is a singleton reporting information on idle time. It is useful not
only for finding out about the current idle time of the PC, but also for getting
notified upon idle time events, such as custom timeouts, or user activity.

%package        devel
Summary:        Build environment for kidletime, an idle time singleton
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for KIdleTime, which is a singleton reporting
information on idle time. It is useful not only for finding out about
the current idle time of the PC, but also for getting notified upon
idle time events, such as custom timeouts, or user activity.

%install -a

%files
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6IdleTime.so.*
%{_kf6_debugdir}/kidletime.categories
%{_kf6_debugdir}/kidletime.renamecategories

%files plugins
%dir %{_kf6_plugindir}/kf6/org.kde.kidletime.platforms
%{_kf6_plugindir}/kf6/org.kde.kidletime.platforms/KF6IdleTimeWaylandPlugin.so
%{_kf6_plugindir}/kf6/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin0.so
%{_kf6_plugindir}/kf6/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin1.so

%files devel
%{_kf6_includedir}/KIdleTime/
%{_kf6_cmakedir}/KF6IdleTime/
%{_kf6_libdir}/libKF6IdleTime.so

%changelog
%autochangelog
