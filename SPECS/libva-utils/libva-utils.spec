# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libva-utils
Version:        2.23.0
Release:        %autorelease
Summary:        Tools for VA-API (vainfo) and test programs
License:        MIT
URL:            https://github.com/intel/libva-utils
VCS:            git:https://github.com/intel/libva-utils.git
#!RemoteAsset:  sha256:fa7ff29847b55010fbbb775b35382f97f29b7b97abe9a2f6fb3e22b36db5440a
Source:         https://github.com/intel/libva-utils/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Ddrm=true
BuildOption(conf):  -Dx11=true
BuildOption(conf):  -Dwayland=true
BuildOption(conf):  -Dtests=false

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva) >= 1.23.0
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-wayland)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)

%description
libva-utils is a collection of utilities and examples for the Video
Acceleration API (VA-API). It includes vainfo, which reports the VA-API
driver and the supported profiles and entrypoints, and a set of
decode, encode and video processing sample programs.

%files
%doc NEWS README.md
%license COPYING
%{_bindir}/*

%changelog
%autochangelog
