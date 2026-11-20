# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtimageformats
%define short_version 6.12

Name:           qt6-qtimageformats
Version:        6.12.0
Release:        %autorelease
Summary:        Qt6 - QtImageFormats component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtimageformats
#!RemoteAsset:  sha256:0943132b5db8de6b6a7f1d162682173e8763c7ed94e80fd39113292845f67762
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -GNinja
BuildOption(conf):  -DFEATURE_mng=ON
BuildOption(conf):  -DFEATURE_jasper=ON

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
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx

%changelog
%autochangelog
