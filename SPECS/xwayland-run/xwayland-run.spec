# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xwayland-run
Version:        0.0.6
Release:        %autorelease
Summary:        Utilities for running Xwayland and headless Wayland compositors
License:        GPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/ofourdan/xwayland-run
VCS:            git:https://gitlab.freedesktop.org/ofourdan/xwayland-run.git
#!RemoteAsset:  sha256:1e597ca87c853ffbbc706230d3301f1c9d4c114ba78bcb704e15a1882ae9caae
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    meson

BuildOption(conf):  -Dcompositor=weston

BuildRequires:  meson >= 0.60.0
BuildRequires:  pkgconfig(python3)

Requires:       Xwayland
Requires:       weston
Requires:       xauth

%description
xwayland-run provides small utilities for running X11 clients on a dedicated
Xwayland server, running Wayland clients on headless compositors, and replacing
xvfb-run with an Xwayland-backed workflow.

%files
%doc README.md
%license COPYING
%{_bindir}/wlheadless-run
%{_bindir}/xwayland-run
%{_bindir}/xwfb-run
%{_mandir}/man1/wlheadless-run.1*
%{_mandir}/man1/xwayland-run.1*
%{_mandir}/man1/xwfb-run.1*
%{_datadir}/wlheadless/
%{python3_sitelib}/wlheadless/

%changelog
%autochangelog
