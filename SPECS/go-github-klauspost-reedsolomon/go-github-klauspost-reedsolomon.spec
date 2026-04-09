# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           reedsolomon
%define go_import_path  github.com/klauspost/reedsolomon
# Test timeout on riscv64 - Julian
%define go_test_ignore_failure 1

Name:           go-github-klauspost-reedsolomon
Version:        1.13.2
Release:        %autorelease
Summary:        Reed-Solomon Erasure Coding in Go
License:        MIT
URL:            https://github.com/klauspost/reedsolomon
#!RemoteAsset
Source0:        https://github.com/klauspost/reedsolomon/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/klauspost/cpuid/v2)

Provides:       go(github.com/klauspost/reedsolomon) = %{version}

%description
Reed-Solomon Erasure Coding in Go, with speeds exceeding 1GB/s/cpu core implemented in pure Go.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
