# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtimageformats
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtimageformats
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - QtImageFormats component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtimageformats
#!RemoteAsset
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(jasper)
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libwebp)

%description
The Qt Image Formats add-on module provides optional support for other
image file formats, including: MNG, TGA, TIFF, WBMP, WEBP, JP2.

%prep -a
rm -rv src/3rdparty

%files
%license LICENSES/GPL* LICENSES/LGPL*
%{_qt6_pluginsdir}/imageformats/libqmng.so
%{_qt6_pluginsdir}/imageformats/libqtga.so
%{_qt6_pluginsdir}/imageformats/libqtiff.so
%{_qt6_pluginsdir}/imageformats/libqwbmp.so
%{_qt6_pluginsdir}/imageformats/libqicns.so
%{_qt6_pluginsdir}/imageformats/libqjp2.so
%{_qt6_pluginsdir}/imageformats/libqwebp.so
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6Gui/*.cmake
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%changelog
%autochangelog
