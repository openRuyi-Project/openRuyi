# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xcb-proto
Version:        1.17.0
Release:        %autorelease
Summary:        XCB protocol descriptions
License:        X11-distribute-modifications-variant
URL:            https://xcb.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/proto/xcbproto.git
#!RemoteAsset
Source0:        https://xorg.freedesktop.org/archive/individual/proto/%{name}-%{version}.tar.xz
BuildArch:      noarch
BuildSystem:    autotools

# Bit of a hack to get the pc file in /usr/share, so we can be noarch.
BuildOption(conf):  --libdir=%{_datadir}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libxml2
BuildRequires:  make
BuildRequires:  pkgconfig(python3)

%description
XCB is a project to enable efficient language bindings to the X11 protocol.
This package contains the protocol descriptions themselves. Language
bindings use these protocol descriptions to generate code for marshalling
the protocol.

%files
%license COPYING
%doc NEWS README.md TODO doc/xml-xcb.txt
%{_datadir}/pkgconfig/xcb-proto.pc
%dir %{_datadir}/xcb/
%{_datadir}/xcb/*.xsd
%{_datadir}/xcb/*.xml
%{python3_sitelib}/xcbgen

%changelog
%autochangelog
