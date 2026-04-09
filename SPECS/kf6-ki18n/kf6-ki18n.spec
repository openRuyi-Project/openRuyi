# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname ki18n
# Full KF6 version (e.g. 6.21.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-ki18n
Version:        6.22.0
Release:        %autorelease
Summary:        KDE Gettext-based UI text internationalization
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            https://invent.kde.org/frameworks/ki18n
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  python3
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KI18n provides functionality for internationalizing user interface text
in applications, based on the GNU Gettext translation system.
It wraps the standard Gettext functionality, so that the programmers
and translators can use the familiar Gettext tools and workflows.

%package        imports
Summary:        QML components for ki18n Framework
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    imports
This package contains QML imports for the ki18n framework.

%package        devel
Summary:        KDE Gettext-based UI text internationalization
Requires:       gettext-runtime
Requires:       gettext-tools
Requires:       kf6-extra-cmake-modules
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description    devel
KI18n provides functionality for internationalizing user interface text
in applications, based on the GNU Gettext translation system.
It wraps the standard Gettext functionality, so that the programmers
and translators can use the familiar Gettext tools and workflows.
Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/ki18n.categories
%{_kf6_debugdir}/ki18n.renamecategories
%{_kf6_plugindir}/kf6/ktranscript.so
%{_kf6_libdir}/libKF6I18n.so.*
%{_kf6_libdir}/libKF6I18nLocaleData.so.*
%{_kf6_libdir}/libKF6I18nQml.so.*
%{_kf6_sharedir}/locale/*/LC_SCRIPTS/ki18n6/
%{_kf6_sharedir}/locale/*/LC_MESSAGES/ki18n6.mo

%files imports
%{_kf6_qmldir}/org/kde/i18n/
%{_kf6_qmldir}/org/kde/ki18n/

%files devel
%{_kf6_includedir}/KI18n/
%{_kf6_includedir}/KI18nLocaleData/
%{_kf6_cmakedir}/KF6I18n/
%{_kf6_libdir}/libKF6I18n.so
%{_kf6_libdir}/libKF6I18nLocaleData.so
%{_kf6_libdir}/libKF6I18nQml.so

%changelog
%autochangelog
