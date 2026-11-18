# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtquicktimeline
%define short_version 6.12

Name:           qt6-qtquicktimeline
Version:        6.12.1
Release:        %autorelease
Summary:        Qt6 - QuickTimeline plugin
License:        GPL-3.0-only AND BSD-3-Clause
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtquicktimeline
#!RemoteAsset:  sha256:2dea872fa020f7f0b12a340127c88108cff00439e54f6bfe61853507e8f01617
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -GNinja

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}

%description
The Qt Quick Timeline plugin provides QML types to use timelines and keyframes
to animate Qt Quick user interfaces.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Quick)

%description    devel
Development files for %{name}.

%files
%license LICENSES/GPL*
%{_qt6_libdir}/libQt6QuickTimeline.so.6*
%{_qt6_libdir}/libQt6QuickTimelineBlendTrees.so.6*
%{_qt6_qmldir}/QtQuick/Timeline/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx

%files devel
%{_qt6_includedir}/QtQuickTimeline/
%{_qt6_includedir}/QtQuickTimelineBlendTrees/
%{_qt6_libdir}/libQt6QuickTimeline.so
%{_qt6_libdir}/libQt6QuickTimeline.prl
%{_qt6_libdir}/libQt6QuickTimelineBlendTrees.so
%{_qt6_libdir}/libQt6QuickTimelineBlendTrees.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6QuickTimeline/
%{_qt6_libdir}/cmake/Qt6QuickTimelinePrivate/
%{_qt6_libdir}/cmake/Qt6QuickTimelineBlendTrees/
%{_qt6_libdir}/cmake/Qt6QuickTimelineBlendTreesPrivate/
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6QuickTimeline.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickTimelineBlendTrees.pc

%changelog
%autochangelog
