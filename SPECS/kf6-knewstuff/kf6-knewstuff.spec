# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname knewstuff
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-knewstuff
Version:        6.22.0
Release:        %autorelease
Summary:        Framework for downloading and sharing additional application data
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://github.com/KDE/knewstuff.git
#!RemoteAsset:  sha256:1f6d4e72d8b66ee93eec8268fadb0d1731716f6a82cb2e46f1ef955c4ef6b1b5
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{_kf6_version}
BuildRequires:  cmake(KF6Attica) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6Package) >= %{_kf6_version}
BuildRequires:  cmake(KF6Syndication) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package        devel
Summary:        Framework for downloading and sharing additional application data
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf6-kirigami >= %{_kf6_version}
Requires:       cmake(KF6Attica) >= %{_kf6_version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description    devel
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification. Development files.

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.knewstuff-dialog6.desktop
%{_kf6_bindir}/knewstuff-dialog6
%{_kf6_debugdir}/knewstuff.categories
%{_kf6_debugdir}/knewstuff.renamecategories
%{_kf6_libdir}/libKF6NewStuffCore.so.*
%{_kf6_libdir}/libKF6NewStuffWidgets.so.*
%{_kf6_qmldir}/org/kde/newstuff/

%files devel
%{_kf6_cmakedir}/KF6NewStuff/
%{_kf6_cmakedir}/KF6NewStuffCore/
%{_kf6_includedir}/KNewStuff/
%{_kf6_includedir}/KNewStuffCore/
%{_kf6_includedir}/KNewStuffWidgets/
%{_kf6_libdir}/libKF6NewStuffCore.so
%{_kf6_libdir}/libKF6NewStuffWidgets.so
%{_kf6_plugindir}/designer/knewstuff6widgets.so

%changelog
%autochangelog
