# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0
%define soversion 0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           knighttime
Version:        6.7.4
Release:        %autorelease
Summary:        Day-night cycle helper library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/knighttime.git
#!RemoteAsset:  sha256:bdc7f327a4b5e21890595a8436a50f08fe49a174e83ef1f9c26b924d411a1b98
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Positioning) >= %{qt6_version}

%description
KNightTime provides helpers for scheduling the dark-light cycle. It can be used to implement
features such as adjusting the screen color temperature based on time of day, etc.

%package        devel
Summary:        Development files for KNightTime
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for KNightTime,  a helper for dark-light day cycles.

%post
%systemd_user_post plasma-knighttimed.service

%preun
%systemd_user_preun plasma-knighttimed.service

%postun
%systemd_user_postun plasma-knighttimed.service

%files
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.knighttimed.desktop
%{_kf6_dbusinterfacesdir}/org.kde.NightTime.xml
%{_kf6_debugdir}/knighttime.categories
%{_kf6_sharedir}/dbus-1/services/org.kde.NightTime.service
%{_libexecdir}/knighttimed
%{_userunitdir}/plasma-knighttimed.service
%{_kf6_libdir}/libKNightTime.so.%{soversion}
%{_kf6_libdir}/libKNightTime.so.*

%files devel
%doc README.md
%{_includedir}/KNightTime/
%{_kf6_cmakedir}/KNightTime/
%{_kf6_libdir}/libKNightTime.so

%changelog
%autochangelog
