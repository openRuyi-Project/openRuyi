# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname ktextwidgets
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-ktextwidgets
Version:        6.22.0
Release:        %autorelease
Summary:        KDE Text editing widgets
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/ktextwidgets
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KTextWidgets provides widgets for displaying and editing text. It supports
rich text as well as plain text.

%package        devel
Summary:        KDE Text editing widgets: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf6-extra-cmake-modules
Requires:       cmake(KF6I18n) >= %{_kf6_version}
Requires:       cmake(KF6Sonnet) >= %{_kf6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description    devel
KTextWidgets provides widgets for displaying and editing text. It supports
rich text as well as plain text. Development files.

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
%{_kf6_libdir}/libKF6TextWidgets.so.*

%files devel
%{_kf6_libdir}/libKF6TextWidgets.so
%{_kf6_cmakedir}/KF6TextWidgets/
%{_kf6_includedir}/KTextWidgets/
%{_kf6_plugindir}/designer/ktextwidgets6widgets.so

%changelog
%autochangelog
