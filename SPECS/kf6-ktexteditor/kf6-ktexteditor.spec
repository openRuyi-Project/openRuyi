# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname ktexteditor
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-ktexteditor
Version:        6.22.0
Release:        %autorelease
Summary:        Embeddable text editor component
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/ktexteditor.git
#!RemoteAsset:  sha256:1d9b336a2b26ecc6a1c5b8133eacea69ed786b3eb6f1ec2ad6705c2bea62e1c5
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DENABLE_KAUTH:BOOL=FALSE
BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(EditorConfig)
BuildRequires:  cmake(KF6Archive) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{_kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{_kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{_kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(libgit2)

Requires:       kf6-syntax-highlighting >= %{_kf6_version}

%description
KTextEditor provides a text editor component that can be embedded in
applications, either as a KPart or using the KF6::TextEditor library.

%package        devel
Summary:        Header files for ktexteditor, an embeddable text editor component
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Parts) >= %{_kf6_version}
Requires:       cmake(KF6SyntaxHighlighting) >= %{_kf6_version}

%description    devel
KTextEditor provides a text editor component that can be embedded in
applications, either as a KPart or using the KF6::TextEditor library.

This subpackage provides the header files.

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/ktexteditor.categories
%{_kf6_debugdir}/ktexteditor.renamecategories
%{_kf6_bindir}/ktexteditor-script-tester6
%{_kf6_libdir}/libKF6TextEditor.so.*
%dir %{_kf6_plugindir}/kf6/parts
%{_kf6_plugindir}/kf6/parts/katepart.so

%files devel
%{_kf6_cmakedir}/KF6TextEditor/
%{_kf6_includedir}/KTextEditor/
%{_kf6_libdir}/libKF6TextEditor.so
%{_kf6_sharedir}/kdevappwizard/templates/ktexteditor6-plugin.tar.bz2

%changelog
%autochangelog
