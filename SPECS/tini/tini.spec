# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tini
Version:        0.19.0
Release:        %autorelease
Summary:        A tiny but valid init for containers
License:        MIT
URL:            https://github.com/krallin/tini
#!RemoteAsset
Source:         https://github.com/krallin/tini/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  glibc-static
BuildRequires:  sed

%description
Tini is the simplest init you could think of.
All Tini does is spawn a single child (Tini is meant to be run in a container),
and wait for it to exit all the while reaping zombies and performing signal
forwarding.

%package        static
Summary:        Standalone static build of %{name}

%description    static
This package contains a standalone static build of %{name}, meant to be used
inside a container.

%files
%license LICENSE
%doc README.md
%{_bindir}/tini

%files static
%license LICENSE
%doc README.md
%{_bindir}/tini-static

%changelog
%autochangelog
