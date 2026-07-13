# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname ktextwidgets
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-ktextwidgets
Version:        6.27.0
Release:        %autorelease
Summary:        KDE Text editing widgets
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/ktextwidgets
#!RemoteAsset:  sha256:03c35d8899559efc17b4f74e86eefd8358dafd7aa9311c89b9c09f7b35700756
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

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

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
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
