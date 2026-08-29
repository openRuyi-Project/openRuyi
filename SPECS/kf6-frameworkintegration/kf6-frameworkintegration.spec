# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname frameworkintegration
# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-frameworkintegration
Version:        6.28.0
Release:        %autorelease
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/frameworkintegration.git
#!RemoteAsset:  sha256:7fdc1db8a5b4c41c7b7487e5e45bc68b0c56a45f182a6362d8bd55ae5f5cc474
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(AppStreamQt) >= 1.0
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{_kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{_kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{_kf6_version}
BuildRequires:  cmake(KF6Package) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(packagekitqt6)
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package        plugin
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Requires:       plasma-integration

%description    plugin
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package        devel
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6ColorScheme) >= %{_kf6_version}
Requires:       cmake(KF6IconThemes) >= %{_kf6_version}
Requires:       cmake(KF6WidgetsAddons) >= %{_kf6_version}

%description    devel
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly. Development files

%files
%doc README.md
%license LICENSES/*
%{_kf6_libdir}/libKF6Style.so.*

%files plugin
%dir %{_kf6_libexecdir}/kpackagehandlers
%{_kf6_libexecdir}/kpackagehandlers/appstreamhandler
%{_kf6_libexecdir}/kpackagehandlers/knshandler
%{_kf6_notificationsdir}/plasma_workspace.notifyrc
%{_kf6_plugindir}/kf6/FrameworkIntegrationPlugin.so

%files devel
%{_kf6_cmakedir}/KF6FrameworkIntegration/
%{_kf6_includedir}/FrameworkIntegration/
%{_kf6_includedir}/KStyle/
%{_kf6_libdir}/libKF6Style.so

%changelog
%autochangelog
