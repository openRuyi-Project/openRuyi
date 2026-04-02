# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname syntax-highlighting
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-syntax-highlighting
Version:        6.22.0
Release:        %autorelease
Summary:        Syntax highlighting engine and library
License:        LGPL-2.1-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND MIT AND BSD-3-Clause AND Artistic-1.0
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/syntax-highlighting.git
#!RemoteAsset:  sha256:50b73ea99413dd988fa34fd169129bcdbfe1dc3b43c48d5f92bbadb2511a728a
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(xerces-c)

%description
This is a tier1/functional version of the Kate syntax highlighting engine.
It's not tied to a particular output format or editor engine.

%package        devel
Summary:        Syntax highlighting engine and library
Requires:       kf6-extra-cmake-modules
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description    devel
This is a tier1/functional version of the Kate syntax highlighting engine.
It's not tied to a particular output format or editor engine.

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/ksyntaxhighlighter6
%{_kf6_debugdir}/ksyntaxhighlighting.categories
%{_kf6_debugdir}/ksyntaxhighlighting.renamecategories
%{_kf6_libdir}/libKF6SyntaxHighlighting.so.*
%{_kf6_qmldir}/org/kde/syntaxhighlighting/

%files devel
%{_kf6_cmakedir}/KF6SyntaxHighlighting/
%{_kf6_includedir}/KSyntaxHighlighting/
%{_kf6_libdir}/libKF6SyntaxHighlighting.so

%changelog
%autochangelog
