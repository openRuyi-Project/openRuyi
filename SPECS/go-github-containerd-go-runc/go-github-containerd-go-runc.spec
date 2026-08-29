# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-runc
%define go_import_path  github.com/containerd/go-runc

Name:           go-github-containerd-go-runc
Version:        1.0.0
Release:        %autorelease
Summary:        Go bindings for runc
License:        Apache-2.0
URL:            https://github.com/containerd/go-runc
#!RemoteAsset:  sha256:c9c1219a63ce0ab7eb3cd2e09bbb6c848dffefbae676dc0087dc1bd45caaa9c0
Source0:        https://github.com/containerd/go-runc/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/containerd/console)
BuildRequires:  go(github.com/opencontainers/runtime-spec)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/containerd/go-runc) = %{version}

Requires:       go(github.com/containerd/console)
Requires:       go(github.com/opencontainers/runtime-spec)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(golang.org/x/sys)

%description
go-runc provides Go bindings for invoking and managing runc.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
