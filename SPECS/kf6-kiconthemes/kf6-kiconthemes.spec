# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kiconthemes
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kiconthemes
Version:        6.22.0
Release:        %autorelease
Summary:        Icon GUI utilities
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kiconthemes
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Archive) >= %{_kf6_version}
BuildRequires:  cmake(KF6BreezeIcons) >= %{_kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks.

%package        devel
Summary:        Icon GUI utilities: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description    devel
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks. Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name}6 --with-qt --all-name --generate-subpackages

%files -f %{name}6.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kiconthemes.categories
%{_kf6_debugdir}/kiconthemes.renamecategories
%dir %{_kf6_plugindir}/kiconthemes6/
%dir %{_kf6_plugindir}/kiconthemes6/iconengines
%{_kf6_plugindir}/kiconthemes6/iconengines/KIconEnginePlugin.so
%{_kf6_libdir}/libKF6IconThemes.so.*
%{_kf6_libdir}/libKF6IconWidgets.so.*
%{_kf6_qmldir}/org/kde/iconthemes/iconthemesplugin.qmltypes
%{_kf6_qmldir}/org/kde/iconthemes/kde-qmlmodule.version
%{_kf6_qmldir}/org/kde/iconthemes/libiconthemesplugin.so
%{_kf6_qmldir}/org/kde/iconthemes/qmldir

%files devel
%{_kf6_bindir}/kiconfinder6
%{_kf6_cmakedir}/KF6IconThemes/
%{_kf6_includedir}/KIconThemes/
%{_kf6_includedir}/KIconWidgets/
%{_kf6_libdir}/libKF6IconThemes.so
%{_kf6_libdir}/libKF6IconWidgets.so
%{_kf6_plugindir}/designer/kiconthemes6widgets.so

%changelog
%autochangelog
