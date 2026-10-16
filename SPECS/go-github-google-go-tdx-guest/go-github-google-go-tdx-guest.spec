# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-tdx-guest
%define go_import_path  github.com/google/go-tdx-guest
# Use a post-release snapshot for the attestation APIs required by TPM tools.
%define commit          23b3eac9db39ba4e1df1426bacb3bfa3a7018e97

Name:           go-github-google-go-tdx-guest
Version:        0.3.1+git20261016.23b3eac
Release:        %autorelease
Summary:        Go libraries for Intel TDX guest attestation
License:        Apache-2.0
URL:            https://github.com/google/go-tdx-guest
#!RemoteAsset:  sha256:07849aeabb91bfc9e68fc345c692147f39700e6ed982fed15e3d20e2a7981bb7
Source0:        https://github.com/google/go-tdx-guest/archive/%{commit}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use decimal formatting for numeric security versions in verification logs.
Patch2000:      2000-verify-format-security-versions-as-integers.patch

BuildOption(prep):  -n %{_name}-%{commit}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-configfs-tsm)
BuildRequires:  go(github.com/google/go-eventlog)
BuildRequires:  go(github.com/google/go-sev-guest)
BuildRequires:  go(github.com/google/go-tpm)
BuildRequires:  go(github.com/google/logger)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/google/go-tdx-guest) = %{version}
Provides:       go(github.com/google/go-tdx-guest/abi) = %{version}
Provides:       go(github.com/google/go-tdx-guest/client) = %{version}
Provides:       go(github.com/google/go-tdx-guest/client/linuxabi) = %{version}
Provides:       go(github.com/google/go-tdx-guest/gce) = %{version}
Provides:       go(github.com/google/go-tdx-guest/pcs) = %{version}
Provides:       go(github.com/google/go-tdx-guest/proto) = %{version}
Provides:       go(github.com/google/go-tdx-guest/proto/checkconfig) = %{version}
Provides:       go(github.com/google/go-tdx-guest/proto/tdx) = %{version}
Provides:       go(github.com/google/go-tdx-guest/rtmr) = %{version}
Provides:       go(github.com/google/go-tdx-guest/testing) = %{version}
Provides:       go(github.com/google/go-tdx-guest/testing/client) = %{version}
Provides:       go(github.com/google/go-tdx-guest/validate) = %{version}
Provides:       go(github.com/google/go-tdx-guest/verify) = %{version}
Provides:       go(github.com/google/go-tdx-guest/verify/dice) = %{version}
Provides:       go(github.com/google/go-tdx-guest/verify/trust) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-configfs-tsm)
Requires:       go(github.com/google/go-eventlog)
Requires:       go(github.com/google/go-sev-guest)
Requires:       go(github.com/google/go-tpm)
Requires:       go(github.com/google/logger)
Requires:       go(go.uber.org/multierr)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/protobuf)

%description
This package collects Intel TDX quotes and verifies quote signatures, certificate chains, and attestation policy.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
