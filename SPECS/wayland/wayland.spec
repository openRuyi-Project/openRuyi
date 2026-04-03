# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <uwu@icenowy.me>
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wayland
Version:        1.25.0
Release:        %autorelease
Summary:        Wayland base protocol library
License:        MIT
URL:            https://wayland.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/wayland/wayland
#!RemoteAsset:  sha256:c065f040afdff3177680600f249727e41a1afc22fccf27222f15f5306faa1f03
Source:         https://gitlab.freedesktop.org/wayland/wayland/-/releases/%{version}/downloads/wayland-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Ddocumentation=false

BuildRequires:  libxml2
BuildRequires:  meson
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libxml-2.0)

%description
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

%package        egl
Summary:        Wayland EGL backend library

%description    egl
This package contains the Wayland EGL backend library, libwayland-egl.

%package        devel
Summary:        Development files for Wayland
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-egl%{?_isa} = %{version}-%{release}

%description    devel
This package contains the headers, libraries and tools needed to develop
Wayland-based applications, including the wayland-scanner tool.

%files
%license COPYING
%{_libdir}/libwayland-client.so.0*
%{_libdir}/libwayland-cursor.so.0*
%{_libdir}/libwayland-server.so.0*

%files egl
%{_libdir}/libwayland-egl.so.1*

%files devel
%{_bindir}/wayland-scanner
%{_includedir}/wayland-*.h
%{_libdir}/libwayland-*.so
%{_libdir}/pkgconfig/wayland-*.pc
%{_datadir}/aclocal/
%{_datadir}/wayland/

%changelog
%{?autochangelog}
