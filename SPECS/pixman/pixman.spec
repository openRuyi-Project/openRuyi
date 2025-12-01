# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pixman
Version:        0.46.4
Release:        %autorelease
Summary:        Pixel manipulation library
License:        MIT
URL:            https://gitlab.freedesktop.org/pixman/pixman
#!RemoteAsset
Source:         https://www.cairographics.org/releases/%{name}-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf): --auto-features=auto

BuildRequires:  meson

%description
Pixman is a pixel manipulation library for X and cairo. This package contains
the runtime shared library.

%package devel
Summary:        Development files for the Pixel Manipulation library
Requires:       %{name} = %{version}

%description devel
This package contains the header files, pkg-config file, and other development
files for the pixman library.

%files
%license COPYING
%{_libdir}/libpixman-1.so.*

%files devel
%{_includedir}/pixman-1
%{_libdir}/libpixman-1.so
%{_libdir}/pkgconfig/pixman-1.pc

%changelog
%{?autochangelog}
