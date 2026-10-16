# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-eventlog
%define go_import_path  github.com/google/go-eventlog
# Use a post-release snapshot for the attestation APIs required by TPM tools.
%define commit          9e88b4ebab1e08c8e6fbabd73f4ccf8587fdc612

Name:           go-github-google-go-eventlog
Version:        0.0.2+git20261016.9e88b4e
Release:        %autorelease
Summary:        Go libraries for parsing and replaying TPM event logs
License:        Apache-2.0
URL:            https://github.com/google/go-eventlog
#!RemoteAsset:  sha256:a6d16f8c54ed7cb3082934a4cb6d927669dbe34d259f18210d390c9bd2f861c6
Source0:        https://github.com/google/go-eventlog/archive/%{commit}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-tpm)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/google/go-eventlog) = %{version}
Provides:       go(github.com/google/go-eventlog/ccel) = %{version}
Provides:       go(github.com/google/go-eventlog/cel) = %{version}
Provides:       go(github.com/google/go-eventlog/extract) = %{version}
Provides:       go(github.com/google/go-eventlog/extract/gmes) = %{version}
Provides:       go(github.com/google/go-eventlog/legacy) = %{version}
Provides:       go(github.com/google/go-eventlog/proto) = %{version}
Provides:       go(github.com/google/go-eventlog/proto/state) = %{version}
Provides:       go(github.com/google/go-eventlog/register) = %{version}
Provides:       go(github.com/google/go-eventlog/tcg) = %{version}
Provides:       go(github.com/google/go-eventlog/tpmeventlog) = %{version}
Provides:       go(github.com/google/go-eventlog/wellknown) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-tpm)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/protobuf)

%description
This package parses TPM event logs, replays measurements, and extracts firmware state for attestation verification.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
