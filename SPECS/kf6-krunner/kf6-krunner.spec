# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname krunner
# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-krunner
Version:        6.28.0
Release:        %autorelease
Summary:        KDE Framework for providing different actions given a string query
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/krunner.git
#!RemoteAsset:  sha256:c4c1fccbe6e04acc8d5891df4eca20a4b6be24c032a10e92839a41c1bb847cc4
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{_kf6_version}
BuildRequires:  cmake(KF6ThreadWeaver) >= %{_kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KDE Framework for providing different actions given a string query.

%package        devel
Summary:        KDE Framework for providing different actions given a string query
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description    devel
Files needed for developing custom runners or frontends.

%files
%doc README.md
%license LICENSES/*
%{_kf6_libdir}/libKF6Runner.so.*
%{_kf6_libdir}/qt6/metatypes/qt6kf6runner_metatypes.json
%{_kf6_debugdir}/krunner.categories
%{_kf6_debugdir}/krunner.renamecategories

%files devel
%{_kf6_cmakedir}/KF6Runner/
%{_kf6_dbusinterfacesdir}/kf6_org.kde.krunner1.xml
%{_kf6_includedir}/KRunner/
%{_kf6_libdir}/libKF6Runner.so
%{_kf6_sharedir}/kdevappwizard/

%changelog
%autochangelog
