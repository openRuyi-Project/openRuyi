# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname knotifyconfig
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-knotifyconfig
Version:        6.27.0
Release:        %autorelease
Summary:        Configuration dialog for desktop notifications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/knotifyconfig.git
#!RemoteAsset:  sha256:81861316d615e7e5ff07143c1d58d9b52cadc5e02ab38c8f2677c01f71e51f26
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Completion) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(libcanberra)

%description
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application.

%package        devel
Summary:        Configuration dialog for desktop notifications
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description    devel
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application. Development files.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_debugdir}/knotifyconfig.categories
%{_kf6_libdir}/libKF6NotifyConfig.so.*

%files devel
%{_kf6_cmakedir}/KF6NotifyConfig/
%{_kf6_includedir}/KNotifyConfig/
%{_kf6_libdir}/libKF6NotifyConfig.so

%changelog
%autochangelog
