# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           platforms
%define go_import_path  github.com/containerd/platforms

Name:           go-github-containerd-platforms
Version:        0.2.1
Release:        %autorelease
Summary:        Go package for container platforms
License:        Apache-2.0
URL:            https://github.com/containerd/platforms
#!RemoteAsset:  sha256:8330cc09017f731c1775892509917e5cf8bcd139f378636deb3ceb6472390e6e
Source0:        https://github.com/containerd/platforms/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/containerd/log)
BuildRequires:  go(github.com/opencontainers/image-spec)

Provides:       go(github.com/containerd/platforms) = %{version}

Requires:       go(github.com/containerd/log)
Requires:       go(github.com/opencontainers/image-spec)

%description
platforms provides helpers for matching and formatting container platform
descriptions.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
