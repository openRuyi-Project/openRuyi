# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           raft
%define go_import_path  github.com/hashicorp/raft

Name:           go-github-hashicorp-raft
Version:        1.3.11
Release:        %autorelease
Summary:        Raft consensus library for Go
License:        MPL-2.0
URL:            https://github.com/hashicorp/raft
#!RemoteAsset:  sha256:f3d98dad1a64bc962348da0f5ffce349f2a701d5c1c06ed3dc8ccc1b7a1ad8c2
Source0:        https://github.com/hashicorp/raft/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix format strings rejected by current Go vet.
Patch2000:      2000-fix-non-constant-format-strings.patch
# Current go-hclog quotes formatted percentage values in text output.
Patch2001:      2001-accept-quoted-snapshot-progress.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/armon/go-metrics)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-msgpack)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/hashicorp/raft) = %{version}

Requires:       go(github.com/armon/go-metrics)
Requires:       go(github.com/hashicorp/go-hclog)
Requires:       go(github.com/hashicorp/go-msgpack)

%description
Raft consensus implementation for replicated logs and finite state
machines, including network transports and snapshot management.

%prep -a
# fuzzy is an independently managed fuzz-test harness (fuzzy/go.mod),
# not part of the public Raft module. Keep the root module tests.
rm -rf fuzzy

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
