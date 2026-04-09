# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bubblewrap
Version:        0.11.0
Release:        %autorelease
Summary:        Core execution tool for unprivileged containers
License:        LGPL-2.0-or-later
URL:            https://github.com/containers/bubblewrap
#!RemoteAsset
Source:         %{url}/releases/download/v%{version}/bubblewrap-%{version}.tar.xz
BuildSystem:    meson

# Temporarily disable man page build since no doc tools are available
BuildOption(conf):  -Dman=disabled

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libselinux)

%description
Bubblewrap (bwrap) is a low-level tool to create sandboxes, using Linux
namespaces to isolate processes. It is a core component of container
technologies like Flatpak.

%files
%license COPYING
%doc README.md
%{_bindir}/bwrap
%{_datadir}/bash-completion/completions/bwrap
%{_datadir}/zsh/site-functions/_bwrap

%changelog
%autochangelog
