# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ebpf
%define go_import_path  github.com/cilium/ebpf
# These tests require eBPF loading privileges, kernel tracing filesystems, or
# host toolchains unavailable in OBS. Compile them separately below.
%define go_test_exclude %{shrink:
    %{go_import_path}
    %{go_import_path}/btf
    %{go_import_path}/cmd/bpf2go
    %{go_import_path}/cmd/bpf2go/gen
    %{go_import_path}/cmd/bpf2go/test
    %{go_import_path}/features
    %{go_import_path}/internal/kallsyms
    %{go_import_path}/internal/linux
    %{go_import_path}/internal/tracefs
    %{go_import_path}/link
    %{go_import_path}/perf
    %{go_import_path}/pin
    %{go_import_path}/ringbuf
}

Name:           go-github-cilium-ebpf
Version:        0.21.0
Release:        %autorelease
Summary:        Go library for eBPF programs
License:        MIT
URL:            https://github.com/cilium/ebpf
#!RemoteAsset:  sha256:1dd0df0edfdfdcc5720c531ff412b66f84b2f6680644346027eba381e946271d
Source0:        https://github.com/cilium/ebpf/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-quicktest/qt)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/jsimonetti/rtnetlink/v2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/cilium/ebpf) = %{version}

Requires:       go(golang.org/x/sys)

%description
ebpf provides pure Go APIs for loading, inspecting, and attaching eBPF
programs.

%check -a
for pkg in %{go_test_exclude}; do
    go test -c -o /dev/null "${pkg}"
done

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
