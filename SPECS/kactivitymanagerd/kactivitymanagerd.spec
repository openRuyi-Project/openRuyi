# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           kactivitymanagerd
Version:        6.5.5
Release:        %autorelease
Summary:        KDE Plasma Activities support
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/plasma/kactivitymanagerd
VCS:            git:https://invent.kde.org/plasma/kactivitymanagerd.git
#!RemoteAsset:  sha256:87a0f8865f180fc69dcab2fe75d9a840fb39c99393c1d37c11a3d3a30171fbf8
Source:         https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  boost-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

Requires:       qt6-qtbase >= %{qt6_version}

Provides:       kactivitymanagerd = %{version}-%{release}
Obsoletes:      kactivitymanagerd < %{version}-%{release}

%description
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
rm -rf $RPM_BUILD_ROOT%{_mandir}/*@*
rm -rf $RPM_BUILD_ROOT%{_kf6_htmldir}/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%post
%systemd_user_post plasma-kactivitymanagerd.service

%preun
%systemd_user_preun plasma-kactivitymanagerd.service

%postun
%systemd_user_postun plasma-kactivitymanagerd.service

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_debugdir}/kactivitymanagerd.categories
%{_kf6_libdir}/libkactivitymanagerd_plugin.so
%{_kf6_plugindir}/kactivitymanagerd1/
%{_kf6_sharedir}/dbus-1/services/org.kde.ActivityManager.service
%{_kf6_sharedir}/krunner/dbusplugins/plasma-runnners-activities.desktop
%{_libexecdir}/kactivitymanagerd
%{_userunitdir}/plasma-kactivitymanagerd.service

%changelog
%autochangelog
