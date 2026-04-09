# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qttranslations
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qttranslations
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - QtTranslations module
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qttranslations
#!RemoteAsset
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Designer)
BuildRequires:  qt6-linguist

%description
QtTranslations contains the translation files for the Qt libraries.

%files
%license LICENSES/*
%{_qt6_translationsdir}/*.qm
%{_qt6_datadir}/translations/catalogs.json
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%changelog
%autochangelog
