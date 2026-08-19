# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-dmverity
%define go_import_path  github.com/containerd/go-dmverity
# These integration tests require root, loop devices, device-mapper, and veritysetup,
# none of which are available in the unprivileged OBS worker.
%define go_test_exclude %{shrink:
    github.com/containerd/go-dmverity/cmd/go-dmverity
    github.com/containerd/go-dmverity/pkg/verity
}

Name:           go-github-containerd-go-dmverity
Version:        0.1.0
Release:        %autorelease
Summary:        Go-dmverity is a containerd sub-project that provides a complete dm-verity implementation in pure Go
License:        Apache-2.0
URL:            https://github.com/containerd/go-dmverity
#!RemoteAsset:  sha256:9d480c2efc65bf166cb8f52a3da08030006469fd281d8a759f196bdcd9b5fc42
Source0:        https://github.com/containerd/go-dmverity/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/containerd/go-dmverity) = %{version}

Requires:       go(github.com/google/uuid)
Requires:       go(golang.org/x/sys)

%description
go-dmverity is a containerd sub-project that provides a complete dm-
verity implementation in pure Go. It enables developers to integrate
dm-verity functionality directly into their Go applications without
requiring external dependencies or system tools.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
