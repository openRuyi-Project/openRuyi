# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-configfs-tsm
%define go_import_path  github.com/google/go-configfs-tsm

Name:           go-github-google-go-configfs-tsm
Version:        0.3.3
Release:        %autorelease
Summary:        Go interface to the Linux Trusted Security Module subsystem
License:        Apache-2.0
URL:            https://github.com/google/go-configfs-tsm
#!RemoteAsset:  sha256:17d5cbb2a4a87f7aa93bef3c3040b28b54c4803bb808221a41b4c4a9f405177e
Source0:        https://github.com/google/go-configfs-tsm/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Format integer register indexes correctly in test failure messages for Go vet.
Patch2000:      2000-tests-format-RTMR-indexes-as-integers.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(go.uber.org/multierr)

Provides:       go(github.com/google/go-configfs-tsm) = %{version}
Provides:       go(github.com/google/go-configfs-tsm/configfs/configfsi) = %{version}
Provides:       go(github.com/google/go-configfs-tsm/configfs/fakertmr) = %{version}
Provides:       go(github.com/google/go-configfs-tsm/configfs/faketsm) = %{version}
Provides:       go(github.com/google/go-configfs-tsm/configfs/linuxtsm) = %{version}
Provides:       go(github.com/google/go-configfs-tsm/report) = %{version}
Provides:       go(github.com/google/go-configfs-tsm/rtmr) = %{version}

Requires:       go(github.com/google/uuid)
Requires:       go(go.uber.org/multierr)

%description
This library wraps the Linux configfs Trusted Security Module interface for
attestation reports and runtime measurement registers. It includes simulated
configfs clients for testing without trusted execution hardware.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
