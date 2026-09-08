# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-m1cpu
%define go_import_path  github.com/shoenig/go-m1cpu
# Tests need Apple IOKit via CGO and cannot run on Linux or riscv64.
%define go_test_ignore_failure 1

Name:           go-github-shoenig-go-m1cpu
Version:        0.2.2
Release:        %autorelease
Summary:        Inspect Apple Silicon CPU frequency from Go
License:        MPL-2.0
URL:            https://github.com/shoenig/go-m1cpu
#!RemoteAsset:  sha256:db639d03716d09cb6fe3eccc273e901627348140c85619132ad0cbef68356501
Source0:        https://github.com/shoenig/go-m1cpu/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/shoenig/test)

Provides:       go(github.com/shoenig/go-m1cpu) = %{version}

%description
go-m1cpu reports performance and efficiency core frequencies for Apple
Silicon CPUs. The implementation uses IOKit through CGO and is Darwin
ARM64 only.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
