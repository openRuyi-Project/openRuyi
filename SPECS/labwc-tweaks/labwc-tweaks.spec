# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           labwc-tweaks
Version:        0.1.0
Release:        %autorelease
Summary:        GUI Configuration app for labwc
License:        BSD-3-Clause AND GPL-2.0-only
URL:            https://github.com/labwc/labwc-tweaks
#!RemoteAsset:  sha256:a742250c7e8ea363758a024688226a4296a6798adc57abe0903d580ab195b749
Source0:        https://github.com/labwc/labwc-tweaks/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(glib-2.0)

Requires:       hicolor-icon-theme
Requires:       labwc

%description
labwc-tweaks is a GUI configuration application for the labwc Wayland compositor.

%install -a
%find_lang %{name} --generate-subpackages --with-qt

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/labwc-tweaks
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/*.xml

%changelog
%autochangelog
