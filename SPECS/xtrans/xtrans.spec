# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xtrans
Version:        1.6.0
Release:        %autorelease
Summary:        X.Org X11 developmental X transport library
License:        HPND AND HPND-sell-variant AND MIT AND MIT-open-group AND X11
URL:            http://www.x.org
VCS:            git:http://gitlab.freedesktop.org/xorg/lib/libxtrans.git
#!RemoteAsset
Source0:        https://www.x.org/releases/individual/lib/%{name}-%{version}.tar.xz
BuildArch:      noarch
BuildSystem:    autotools

Patch0:         xtrans-1.0.3-avoid-gethostname.patch

# yes, this looks horrible, but it's to get the .pc file in datadir
BuildOption(conf):  --libdir=%{_datadir}
BuildOption(conf):  --disable-docs

BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  util-macros

%description
X.Org X11 developmental X transport library

%files
%license COPYING
%doc AUTHORS ChangeLog README.md doc/*.xml
%dir %{_includedir}/X11
%{_includedir}/X11/Xtrans
%{_datadir}/aclocal/xtrans.m4
%{_datadir}/pkgconfig/xtrans.pc

%changelog
%autochangelog
