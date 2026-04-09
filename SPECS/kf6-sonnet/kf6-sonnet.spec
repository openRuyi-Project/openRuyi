# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname sonnet
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-sonnet
Version:        6.22.0
Release:        %autorelease
Summary:        KDE spell checking library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/sonnet
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libvoikko)

%description
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.

%package        devel
Summary:        KDE spell checking library: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description    devel
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports different plugins, including
HSpell, Enchant, ASpell and HUNSPELL. Development files.

%package        voikko
Summary:        voikko plugin for %{name}
Supplements:    (%{name} and langpacks-fi)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    voikko
The %{name}-voikko package contains the Finnish voikko spellchecking
plugin for %{name}.

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
%dir %{_kf6_plugindir}/kf6/sonnet
%{_kf6_debugdir}/sonnet.categories
%{_kf6_debugdir}/sonnet.renamecategories
%{_kf6_plugindir}/kf6/sonnet/sonnet_hunspell.so
%{_kf6_libdir}/libKF6SonnetCore.so.*
%{_kf6_libdir}/libKF6SonnetUi.so.*
%{_kf6_qmldir}/org/kde/sonnet/

%files devel
%{_kf6_bindir}/parsetrigrams6
%{_kf6_cmakedir}/KF6Sonnet/
%{_kf6_includedir}/Sonnet/
%{_kf6_includedir}/SonnetCore/
%{_kf6_includedir}/SonnetUi/
%{_kf6_libdir}/libKF6SonnetCore.so
%{_kf6_libdir}/libKF6SonnetUi.so
%{_kf6_plugindir}/designer/sonnet6widgets.so

%files voikko
%{_kf6_plugindir}/kf6/sonnet/sonnet_voikko.so

%changelog
%autochangelog
