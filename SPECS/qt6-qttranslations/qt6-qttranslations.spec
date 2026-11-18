# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qttranslations
%define short_version 6.12

Name:           qt6-qttranslations
Version:        6.12.1
Release:        %autorelease
Summary:        Qt6 - QtTranslations module
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qttranslations
#!RemoteAsset:  sha256:5d537a0b849df9a0586fb20435ce232bc3e21e95025134f6ea8f5cc19622158a
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -GNinja

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Linguist) >= %{version}
BuildRequires:  qt6-linguist >= %{version}

%description
QtTranslations contains the translation files for the Qt libraries.

%files
%license LICENSES/*
%{_qt6_translationsdir}/*.qm
%{_qt6_datadir}/translations/catalogs.json
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx

%changelog
%autochangelog
