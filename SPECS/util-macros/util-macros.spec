# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           util-macros
Version:        1.20.2
Release:        %autorelease
Summary:        Utility Macro Headers for X.Org development
License:        MIT
URL:            https://xorg.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/util/macros.git
#!RemoteAsset
Source:         https://www.x.org/releases/individual/util/util-macros-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(build):  CFLAGS="%{optflags} -fno-strict-aliasing"

BuildRequires:  pkgconfig
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
This package provides a set of common Autoconf macros used throughout the
X.Org build system.

%install -a
rm -f %{buildroot}%{_datadir}/util-macros/INSTALL

%files
%license COPYING
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/*.m4
%{_datadir}/pkgconfig/*.pc

%changelog
%autochangelog
