# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           kglobalacceld
Version:        6.7.4
Release:        %autorelease
Summary:        Global keyboard shortcut daemon
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/kglobalacceld.git
#!RemoteAsset:  sha256:b25f49e86560cc25c97c12b18f81b5e5692aa6e91b8d214473d4ce286026bece
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xkb)

%description
Daemon providing Global Keyboard Shortcut (Accelerator) functionality.

%package        devel
Summary:        Global keyboard shortcut daemon: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description    devel
Daemon providing Global Keyboard Shortcut (Accelerator) functionality.
Development files.

%post
%systemd_user_post plasma-kglobalaccel.service

%preun
%systemd_user_preun plasma-kglobalaccel.service

%postun
%systemd_user_postun plasma-kglobalaccel.service

%files
%license LICENSES/*
%{_kf6_configdir}/autostart/kglobalacceld.desktop
%{_kf6_debugdir}/kglobalacceld.categories
%dir %{_kf6_plugindir}/org.kde.kglobalacceld.platforms
%{_kf6_plugindir}/org.kde.kglobalacceld.platforms/KGlobalAccelDXcb.so
%{_kf6_libdir}/libKGlobalAccelD.so.*
%{_libexecdir}/kglobalacceld
%{_userunitdir}/plasma-kglobalaccel.service

%files devel
%{_kf6_cmakedir}/KGlobalAccelD/
%{_includedir}/KGlobalAccelD/

%changelog
%autochangelog
