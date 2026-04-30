# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond xwayland 0

Name:           wlroots
Version:        0.19.3
Release:        %autorelease
Summary:        A modular Wayland compositor library
License:        MIT
URL:            https://gitlab.freedesktop.org/wlroots/wlroots
#!RemoteAsset:  sha256:a6ff89b64ea15e424d1b0db4a22145fccf5ec2ff2e7b8af0fa35e2ac8975986f
Source0:        https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/%{version}/wlroots-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dexamples=false
BuildOption(conf):  -Dxwayland=disabled
BuildOption(conf):  -Dbackends=drm,libinput

BuildRequires:  meson >= 1.3
BuildRequires:  gcc
BuildRequires:  glslang
BuildRequires:  pkgconfig(libliftoff)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm) >= 2.4.122
BuildRequires:  pkgconfig(libinput) >= 1.21.0
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1) >= 0.43.0
BuildRequires:  pkgconfig(vulkan) >= 1.2.182
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.41
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.23.1
BuildRequires:  pkgconfig(xkbcommon)
%if %{with xwayland}
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-renderutil)
%endif
Provides:       wlroots-0.19

%description
wlroots is a modular Wayland compositor library. It implements a huge number of
Wayland protocols and features.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     pkgconfig(xcb-icccm)

%description    devel
Development files for %{name}.

%files
%license LICENSE
%doc README.md
%{_libdir}/libwlroots-*.so

%files devel
%{_includedir}/wlroots-*/
%{_libdir}/pkgconfig/wlroots-0.19.pc

%changelog
%autochangelog
