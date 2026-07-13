# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.15.0
%define qt6_version 6.6.0

Name:           kirigami-addons
Version:        1.12.1
Release:        %autorelease
Summary:        Add-ons for the Kirigami framework
License:        LGPL-3.0-only
URL:            https://www.kde.org
VCS:            https://invent.kde.org/libraries/kirigami-addons.git
#!RemoteAsset:  sha256:c543a493ce5875f405fb1c9ff6d531060ed082cc6d710e56d46ac42d164207bb
Source:         https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Tools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

Requires:       kf6-kirigami >= %{kf6_version}
Requires:       kf6-ksvg >= %{kf6_version}

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%package        devel
Summary:        Development files for kirigami-addons
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma). This package provides development files to build
applications with kirigami-addons.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_qmldir}/org/kde/kirigamiaddons/
%{_kf6_libdir}/libKirigamiAddonsStatefulApp.so.*
%{_kf6_libdir}/libKirigamiApp.so.*
%{_kf6_libdir}/libKirigamiAddonsComponents.so.*

%files devel
%{_kf6_cmakedir}/KF6KirigamiAddons/
%{_includedir}/KirigamiAddons/
%{_includedir}/KirigamiAddonsStatefulApp/
%{_kf6_libdir}/libKirigamiAddonsStatefulApp.so
%{_kf6_libdir}/libKirigamiApp.so
%{_kf6_libdir}/libKirigamiAddonsComponents.so
%dir %{_kf6_sharedir}/kdevappwizard/
%dir %{_kf6_sharedir}/kdevappwizard/templates/
%{_kf6_sharedir}/kdevappwizard/templates/kirigamiaddons6.tar.bz2
%{_kf6_sharedir}/kdevappwizard/templates/librarymanager6.tar.bz2

%changelog
%autochangelog
