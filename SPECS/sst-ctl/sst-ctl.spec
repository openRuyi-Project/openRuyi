# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goresctrl
%define go_import_path  github.com/intel/goresctrl

%ifarch x86_64
# Some tests need Intel SST hardware or writable cgroup filesystems.
%define go_test_ignore_failure 1
%else
# The SST command and package use amd64-only kernel types. Other architectures
# build and test the remaining goresctrl packages.
%define go_test_exclude %{shrink:
    %{go_import_path}/cmd/sst-ctl
    %{go_import_path}/pkg/sst
}
%endif

Name:           sst-ctl
Version:        0.5.0
Release:        %autorelease
Summary:        Command-line utility for managing Intel Speed Select Technology
License:        Apache-2.0
URL:            https://github.com/intel/goresctrl
#!RemoteAsset:  sha256:62fd444152b81dcbac1d21d1b47340464359146b3292dfb1b6d7ee5853ea5afa
Source0:        https://github.com/intel/goresctrl/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/opencontainers/runtime-spec)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(sigs.k8s.io/yaml)

%description
sst-ctl queries and configures Intel Speed Select Technology base-frequency,
core-power, and CLOS settings. The command is available on x86_64 systems.

%package     -n go-github-intel-goresctrl
Summary:        Go library for managing Linux resource controls
BuildArch:      noarch
Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/opencontainers/runtime-spec)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(golang.org/x/sys)
Requires:       go(k8s.io/apimachinery)
Requires:       go(sigs.k8s.io/yaml)

%description -n go-github-intel-goresctrl
goresctrl provides Go helpers for managing Linux resource-control filesystems.

%prep -a
%go_prep

%build -a
%ifarch x86_64
%go_common
cd %{_builddir}/go/src/%{go_import_path}
%__go build %{go_build_flags_default} -o %{_builddir}/sst-ctl ./cmd/sst-ctl
%endif

%install -a
%ifarch x86_64
install -D -m 0755 %{_builddir}/sst-ctl %{buildroot}%{_bindir}/sst-ctl
%endif

%check -a
%ifarch x86_64
%go_common
cd %{_builddir}/go/src/%{go_import_path}
# Keep compilation failures fatal when hardware-dependent tests are tolerated.
%__go test -vet=off -run '^$' ./...
%endif

%ifarch x86_64
%files
%doc README.md
%license LICENSE
%{_bindir}/sst-ctl
%endif

%files -n go-github-intel-goresctrl
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
