# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xcb-imdkit
Version:        1.0.9
Release:        %autorelease
Summary:        Input method development support for xcb
License:        LGPL-2.1-only AND MIT
URL:            https://github.com/fcitx/xcb-imdkit
#!RemoteAsset:  sha256:74283bacef4d53655d3ddd6e3b969a787f77ee9d66b6ef256a2012a6ba2d1104
Source0:        https://download.fcitx-im.org/fcitx5/xcb-imdkit/xcb-imdkit-%{version}.tar.zst
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)

%description
xcb-imdkit is an implementation of xim protocol in xcb,
comparing with the implementation of IMDkit with Xlib,
and xim inside Xlib, it has less memory foot print,
better performance, and safer on malformed client.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%files
%doc README.md
%license LICENSES/LGPL-2.1-only.txt
%{_libdir}/libxcb-imdkit.so.1*

%files devel
%{_includedir}/xcb-imdkit/
%{_libdir}/cmake/XCBImdkit/
%{_libdir}/libxcb-imdkit.so
%{_libdir}/pkgconfig/xcb-imdkit.pc

%changelog
%autochangelog
