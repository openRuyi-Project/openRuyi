# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-tpm
%define go_import_path  github.com/google/go-tpm

# Seed the source dependency cycle without changing the go-tpm test selection.
%bcond bootstrap 0

# Keep integration tests requiring the optional Microsoft TPM simulator out of
# the OBS test run, while shipping the simulator transport package for consumers.
%define go_test_exclude %{shrink:
    %{go_import_path}/legacy/tpm2/test
    %{go_import_path}/tpm2
    %{go_import_path}/tpm2/test
}

Name:           go-github-google-go-tpm
Version:        0.9.8
Release:        %autorelease
Summary:        Go library for communicating with TPM devices
License:        Apache-2.0
URL:            https://github.com/google/go-tpm
#!RemoteAsset:  sha256:93b44f860c962bc92b7ab5af4d9b19b2e497e1e46a14a9a7500af13f46742587
Source0:        https://github.com/google/go-tpm/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# Stage the complete tools repository only when bootstrapping its simulator.
#!RemoteAsset:  sha256:050823ea0aa7bcc14a31f090ffb79bbb9ec5d96fadbb0094e63e75636b67fbe9
Source1:        https://github.com/google/go-tpm-tools/archive/v0.4.11.tar.gz#/go-tpm-tools-0.4.11.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use hexadecimal verbs for TPM handles so current Go vet accepts the example.
Patch2000:      2000-format-tpm-handle-errors.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
# The simulator transport compiles the reference TPM C code against OpenSSL.
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  go(github.com/google/go-cmp)
%if %{without bootstrap}
BuildRequires:  go(github.com/google/go-tpm-tools/simulator)
%endif
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/google/go-tpm) = %{version}
Provides:       go(github.com/google/go-tpm/tpm2/transport/simulator) = %{version}

%if %{without bootstrap}
Requires:       go(github.com/google/go-tpm-tools/simulator)
%endif
Requires:       go(golang.org/x/sys)

%description
Go-TPM provides Go libraries for communicating directly with TPM 1.2 and TPM
2.0 devices on Linux and Windows.

%if %{with bootstrap}
# Preserve the full dependency tree in the test GOPATH without installing it.
# Only go-tpm owns this RPM; the complete tools producer is built separately.
%prep -a
mkdir -p %{_builddir}/go/src/github.com/google/go-tpm-tools
tar -xf %{SOURCE1} --strip-components=1 -C %{_builddir}/go/src/github.com/google/go-tpm-tools
%endif

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
