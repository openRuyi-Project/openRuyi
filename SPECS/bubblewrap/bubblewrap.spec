# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bubblewrap
Version:        0.13.1
Release:        %autorelease
Summary:        Core execution tool for unprivileged containers
License:        LGPL-2.1-or-later
URL:            https://github.com/containers/bubblewrap
#!RemoteAsset:  sha256:0e85c8702248b8dd64144f594147553650cdd0e4c951690345faace79c217c4d
Source:         %{url}/releases/download/v%{version}/bubblewrap-%{version}.tar.xz
BuildSystem:    meson

# Temporarily disable man page build since no doc tools are available
BuildOption(conf):  -Dman=disabled

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
%{bash_completions_dir}/bwrap
%{zsh_completions_dir}/_bwrap

%changelog
%autochangelog
