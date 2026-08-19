# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           plugin
%define go_import_path  github.com/containerd/plugin

Name:           go-github-containerd-plugin
Version:        1.1.0
Release:        %autorelease
Summary:        A Go package providing a common plugin interface across containerd repositories
License:        Apache-2.0
URL:            https://github.com/containerd/plugin
#!RemoteAsset:  sha256:db2763e318531594bc5151cacfaacc961df28119f374c9afa1e49eccadc2a710
Source0:        https://github.com/containerd/plugin/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/opencontainers/image-spec)

Provides:       go(github.com/containerd/plugin) = %{version}

Requires:       go(github.com/opencontainers/image-spec)

%description
A Go package providing a common plugin interface across containerd
repositories.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
