# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kcolorscheme
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kcolorscheme
Version:        6.27.0
Release:        %autorelease
Summary:        Classes to read and interact with KColorScheme
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kcolorscheme
#!RemoteAsset:  sha256:574e12350ea1adf248c5263cf18d145476d368664a302514d1065aa2563e1efd
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Codecs) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
Classes to read and interact with KColorScheme.

%package        devel
Summary:        Classes to read and interact with KColorScheme: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6GuiAddons) >= %{_kf6_version}
Requires:       cmake(KF6I18n) >= %{_kf6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description    devel
Classes to read and interact with KColorScheme. Development files.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kcolorscheme.categories
%{_kf6_libdir}/libKF6ColorScheme.so.*

%files devel
%{_kf6_cmakedir}/KF6ColorScheme/
%{_kf6_includedir}/KColorScheme/
%{_kf6_libdir}/libKF6ColorScheme.so

%changelog
%autochangelog
