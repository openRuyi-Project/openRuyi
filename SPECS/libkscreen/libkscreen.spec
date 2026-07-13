# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

%define sover 8

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           libkscreen
Version:        6.7.1
Release:        %autorelease
Summary:        Plasma screen management library
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/libkscreen.git
#!RemoteAsset:  sha256:4c2d80b327e97154b8051239e51037f92568d6dcc08d26f52d59627ec432460f
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DBUILD_QCH:BOOL=TRUE

BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  qt6-qtwayland-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.10.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  python
BuildRequires:  pkgconfig(wayland-client) >= 1.9
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)

%description
Dynamic display management library for KDE

%package        plugin
Summary:        Plasma screen management library
Requires:       %{name}-devel = %{version}-%{release}
Provides:       libkscreen2-plugin = %{version}
Obsoletes:      libkscreen2-plugin < %{version}

%description    plugin
Plugins for dynamic display management in Plasma

%package        devel
Summary:        Plasma screen management library (development package)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description    devel
Development files belonging to libkscreen, dynamic display management in Plasma

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%post plugin
%systemd_user_post plasma-kscreen.service

%preun plugin
%systemd_user_preun plasma-kscreen.service

%postun plugin
%systemd_user_postun plasma-kscreen.service

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_libdir}/libKF6Screen.so.%{sover}
%{_kf6_libdir}/libKF6Screen.so.%{version}
%{_kf6_libdir}/libKF6ScreenDpms.so.%{sover}
%{_kf6_libdir}/libKF6ScreenDpms.so.%{version}

%files plugin
%{_kf6_bindir}/kscreen-doctor
%{_kf6_plugindir}/kf6/kscreen/
%{_kf6_libexecdir}/kscreen_backend_launcher
%{_kf6_sharedir}/dbus-1/services/org.kde.kscreen.service
%{_kf6_debugdir}/libkscreen.categories
%{_userunitdir}/plasma-kscreen.service
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_kscreen-doctor

%files devel
%doc %{_kf6_qchdir}/KF6Screen.*
%{_kf6_includedir}/kscreen_version.h
%{_kf6_includedir}/KScreen/
%{_kf6_libdir}/cmake/KF6Screen/
%{_kf6_libdir}/libKF6Screen.so
%{_kf6_libdir}/libKF6ScreenDpms.so
%{_kf6_libdir}/pkgconfig/KF6Screen.pc

%changelog
%autochangelog
