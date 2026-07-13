# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

%global _smp_ncpus_max 4

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           kscreenlocker
Version:        6.7.1
Release:        %autorelease
Summary:        Library and components for secure lock screen architecture
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/kscreenlocker.git
#!RemoteAsset:  sha256:7555a26dfd985310faa2753c4d3eba9591b56045ab4a73efd8b6249b241d9661
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        kde
Source2:        kde-fingerprint
Source3:        kde-smartcard
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  cmake >= 3.16
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Screen) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LayerShellQt) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.46
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)

Provides:       qt6qmlimport(org.kde.kscreenlocker.1) = 0

Obsoletes:      kscreenlocker < %{version}
Obsoletes:      kscreenlocker-lang < %{version}

%description
Library and components for secure lock screen architecture.

%package        devel
Summary:        Library and components for secure lock screen architecture - development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Conflicts:      kscreenlocker-devel

%description    devel
Development files for Library and components for secure lock screen architecture.

%install -a
install -D -m0644 %{SOURCE1} %{buildroot}%{_pam_confdir}/kde
install -D -m0644 %{SOURCE2} %{buildroot}%{_pam_confdir}/kde-fingerprint
install -D -m0644 %{SOURCE3} %{buildroot}%{_pam_confdir}/kde-smartcard

# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_screenlocker.desktop
%{_kf6_debugdir}/kscreenlocker.categories
%{_kf6_notificationsdir}/ksmserver.notifyrc
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_screenlocker.so
%{_kf6_sharedir}/ksmserver/
%{_libexecdir}/kscreenlocker_greet
%{_pam_confdir}/kde
%{_pam_confdir}/kde-fingerprint
%{_pam_confdir}/kde-smartcard
%{_kf6_libdir}/libKScreenLocker.so.*

%files devel
%{_includedir}/KScreenLocker/
%{_kf6_cmakedir}/KScreenLocker/
%{_kf6_cmakedir}/ScreenSaverDBusInterface/
%{_kf6_libdir}/libKScreenLocker.so
%{_kf6_sharedir}/dbus-1/interfaces/kf6_org.freedesktop.ScreenSaver.xml
%{_kf6_sharedir}/dbus-1/interfaces/org.kde.screensaver.xml

%changelog
%autochangelog
