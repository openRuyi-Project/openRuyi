# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtquickeffectmaker
%define short_version 6.12

Name:           qt6-qtquickeffectmaker
Version:        6.12.1
Release:        %autorelease
Summary:        Tool for creating shader effects for Qt Quick
License:        GPL-3.0-only AND BSD-3-Clause AND OFL-1.1
URL:            https://doc.qt.io/qt-6/qtquickeffectmaker-index.html
VCS:            git:https://github.com/qt/qtquickeffectmaker
#!RemoteAsset:  sha256:9dad8295b7bdd1bdb02a2d25f6c9dafb2d4bcdfcbf4de78fc0879f09f1933cb1
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
Source1:        quickeffectmaker.desktop
BuildSystem:    cmake

BuildOption(conf):  -GNinja
BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6ShaderTools)
BuildRequires:  pkgconfig(Qt6Quick3D)
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig

%description
Qt Quick Effect Maker (QQEM) is a tool for creating custom shader effects for
Qt Quick. It provides a node-based visual editor to design effects and exports
them as QML components.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%install -a
desktop-file-install --dir=%{buildroot}%{_datadir}/applications --vendor="qt6" %{SOURCE1}

%files
%license LICENSES/GPL-3.0-only.txt
%{_qt6_bindir}/qqem
%{_qt6_qmldir}/QtQuickEffectMaker/
%{_qt6_archdatadir}/sbom/qqeffectmaker-%{version}.spdx
%{_datadir}/applications/*.desktop

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
