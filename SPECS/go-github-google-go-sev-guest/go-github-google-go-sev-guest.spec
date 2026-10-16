# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-sev-guest
%define go_import_path  github.com/google/go-sev-guest

Name:           go-github-google-go-sev-guest
Version:        0.15.0
Release:        %autorelease
Summary:        Go libraries for AMD SEV-SNP guest attestation
License:        Apache-2.0
URL:            https://github.com/google/go-sev-guest
#!RemoteAsset:  sha256:2b7694e77cebbb32788cd91a256a55d9aebe6fd30cb69887596058c99e88d17f
Source0:        https://github.com/google/go-sev-guest/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/google/go-sev-guest/pull/204
Patch1000:      1000-abi-prevent-certificate-table-integer-overflow.patch
# Use the appropriate format verb for certificate function enums in test helpers.
Patch2000:      2000-testing-format-certificate-function-values.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-configfs-tsm)
BuildRequires:  go(github.com/google/logger)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/google/go-sev-guest) = %{version}
Provides:       go(github.com/google/go-sev-guest/abi) = %{version}
Provides:       go(github.com/google/go-sev-guest/client) = %{version}
Provides:       go(github.com/google/go-sev-guest/client/linuxabi) = %{version}
Provides:       go(github.com/google/go-sev-guest/kds) = %{version}
Provides:       go(github.com/google/go-sev-guest/proto) = %{version}
Provides:       go(github.com/google/go-sev-guest/proto/check) = %{version}
Provides:       go(github.com/google/go-sev-guest/proto/fakekds) = %{version}
Provides:       go(github.com/google/go-sev-guest/proto/sevsnp) = %{version}
Provides:       go(github.com/google/go-sev-guest/testing) = %{version}
Provides:       go(github.com/google/go-sev-guest/testing/client) = %{version}
Provides:       go(github.com/google/go-sev-guest/testing/data) = %{version}
Provides:       go(github.com/google/go-sev-guest/tools/lib/cmdline) = %{version}
Provides:       go(github.com/google/go-sev-guest/tools/lib/report) = %{version}
Provides:       go(github.com/google/go-sev-guest/validate) = %{version}
Provides:       go(github.com/google/go-sev-guest/verify) = %{version}
Provides:       go(github.com/google/go-sev-guest/verify/trust) = %{version}

Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-configfs-tsm)
Requires:       go(github.com/google/logger)
Requires:       go(github.com/google/uuid)
Requires:       go(go.uber.org/multierr)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/xerrors)
Requires:       go(google.golang.org/protobuf)

%description
This package collects AMD SEV-SNP attestation reports and verifies report signatures, certificate chains, and policy constraints.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
