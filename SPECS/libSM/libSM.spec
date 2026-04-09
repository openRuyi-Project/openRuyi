# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libSM
Version:        1.2.6
Release:        %autorelease
Summary:        X.Org X11 SM runtime library
License:        MIT AND MIT-open-group
URL:            http://www.x.org
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libsm.git
#!RemoteAsset
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --with-libuuid
BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ice) >= 1.0.5
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  util-macros

%description
The X.Org X11 SM (Session Management) runtime library.

%package        devel
Summary:        X.Org X11 SM development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The X.Org X11 SM (Session Management) development package.

%files
%{_libdir}/libSM.so.6*
%doc %{_docdir}/%{name}

%files          devel
%{_includedir}/X11/*
%{_libdir}/libSM.so
%{_libdir}/pkgconfig/sm.pc
%license COPYING
%doc README.md

%changelog
%autochangelog
