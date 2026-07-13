# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kbookmarks
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kbookmarks
Version:        6.27.0
Release:        %autorelease
Summary:        Framework for manipulating bookmarks in XBEL format
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kbookmarks
#!RemoteAsset:  sha256:75a43775ef03cb0c577c70d9605203789b3c75b786efa17a2e8c286d0c55fb93
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
This is a framework for accessing and manipulating bookmarks using
the XBEL format.

%package        devel
Summary:        Development files for kbookmarks, a XBEL format bookmark manipulation framework
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6WidgetsAddons) >= %{_kf6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}

%description    devel
Development files for kbookmarks, a framework for accessing and
manipulating bookmarks using the XBEL format

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kbookmarks.categories
%{_kf6_debugdir}/kbookmarks.renamecategories
%{_kf6_debugdir}/kbookmarkswidgets.categories
%{_kf6_libdir}/libKF6Bookmarks.so.*
%{_kf6_libdir}/libKF6BookmarksWidgets.so.*

%files devel
%{_kf6_libdir}/libKF6Bookmarks.so
%{_kf6_libdir}/libKF6BookmarksWidgets.so
%{_kf6_cmakedir}/KF6Bookmarks/
%{_kf6_includedir}/KBookmarks/
%{_kf6_includedir}/KBookmarksWidgets/

%changelog
%autochangelog
