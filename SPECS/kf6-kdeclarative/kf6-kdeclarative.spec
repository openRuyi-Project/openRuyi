# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kdeclarative
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kdeclarative
Version:        6.22.0
Release:        %autorelease
Summary:        Integration of QML and KDE workspaces
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kdeclarative.git
#!RemoteAsset:  sha256:055a97da106cdc1f8796cb90cdd262c8f88c41522ef5e86068c3ce7dc28c4be7
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{_kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KDeclarative provides integration of QML and KDE workspaces.

%package        devel
Summary:        Integration of QML and KDE workspaces: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf6-kirigami >= %{_kf6_version}
Requires:       cmake(KF6Config) >= %{_kf6_version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_version}
Requires:       cmake(Qt6Quick) >= %{qt6_version}

%description    devel
KDeclarative provides integration of QML and KDE workspaces.
Development files.

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6CalendarEvents.so.*
%dir %{_kf6_qmldir}/org/
%dir %{_kf6_qmldir}/org/kde/
%{_kf6_qmldir}/org/kde/draganddrop/
%{_kf6_qmldir}/org/kde/graphicaleffects/
%{_kf6_qmldir}/org/kde/kquickcontrols/
%{_kf6_qmldir}/org/kde/private/kquickcontrols/
%{_kf6_qmldir}/org/kde/kquickcontrolsaddons/
%{_kf6_libdir}/libkquickcontrolsprivate.so.0
%{_kf6_libdir}/libkquickcontrolsprivate.so.%{version}

%files devel
%{_kf6_cmakedir}/KF6Declarative/
%{_kf6_includedir}/KDeclarative/
%{_kf6_libdir}/libKF6CalendarEvents.so

%changelog
%autochangelog
