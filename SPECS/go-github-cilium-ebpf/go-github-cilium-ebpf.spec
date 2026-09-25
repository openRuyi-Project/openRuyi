# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ebpf
%define go_import_path  github.com/cilium/ebpf
# eBPF program-loading tests require capabilities unavailable in OBS.
%define go_test_ignore_failure 1

Name:           go-github-cilium-ebpf
Version:        0.22.0
Release:        %autorelease
Summary:        Go library for eBPF programs
License:        MIT
URL:            https://github.com/cilium/ebpf
#!RemoteAsset:  sha256:82be23c4cab66f0911a6ff4ed225a0abd9a05c51475f0098b8d8d0ad1490631a
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

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
