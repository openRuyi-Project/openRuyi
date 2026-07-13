# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           kmenuedit
Version:        6.7.1
Release:        %autorelease
Summary:        Provides the interface and basic tools for the KDE workspace
License:        GPL-2.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/kmenuedit.git
#!RemoteAsset:  sha256:7225f2d9a8ea683bf29eb4fd3bffea583a8d10e37fa1a2b4004c8bd3aff3cf28
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds

%description
Provides the interface and basic tools for the KDE workspace.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --with-html --all-name --generate-subpackages

%files -f %{name}.lang
%doc %lang(en) %{_kf6_htmldir}/en/kmenuedit/
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.kmenuedit.desktop
%{_kf6_appstreamdir}/org.kde.kmenuedit.appdata.xml
%{_kf6_bindir}/kmenuedit
%{_kf6_debugdir}/kmenuedit.categories
%{_kf6_iconsdir}/hicolor/*/apps/kmenuedit.png
%{_kf6_sharedir}/kmenuedit/

%changelog
%autochangelog
