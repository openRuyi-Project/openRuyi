# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname qqc2-desktop-style
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-qqc2-desktop-style
Version:        6.27.0
Release:        %autorelease
Summary:        A Qt Quick Controls 2 Style for Desktop UIs
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/qqc2-desktop-style.git
#!RemoteAsset:  sha256:6c005f06c5f8c4ac349238abf14999bb917215a8f7b8c51364e2fdd12e9e6355
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{_kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

Requires:       kf6-sonnet >= %{_kf6_version}
# Qt QML runtime imports are provided by qt6-qtdeclarative itself
Requires:       qt6-qtdeclarative >= %{qt6_version}

%description
A Qt Quick Controls 2 style engine that uses the desktop style
to draw controls with QStyle.

%package        devel
Summary:        Development Files for Qt Quick Controls 2 Desktop Style
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This file contains cmake files to be used by projects that depend on
qqc2-desktop-style.
Usually not needed as it is only a runtime dependency.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%dir %{_kf6_plugindir}/kf6/kirigami
%dir %{_kf6_plugindir}/kf6/kirigami/platform
%{_kf6_plugindir}/kf6/kirigami/platform/org.kde.desktop.so
%{_kf6_qmldir}/org/kde/desktop/
%{_kf6_qmldir}/org/kde/qqc2desktopstyle/

%files devel
%{_kf6_cmakedir}/KF6QQC2DesktopStyle/

%changelog
%autochangelog
