# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           base64x
%define go_import_path  github.com/cloudwego/base64x
# bench tests require an unpackaged third-party comparison implementation.
# internal/rt has no riscv64 implementation for its assembly helper.
%define go_test_exclude %{shrink:
    %{go_import_path}/bench
    %{go_import_path}/internal/rt
}

Name:           go-github-cloudwego-base64x
Version:        0.1.7
Release:        %autorelease
Summary:        High-performance replacement for Go encoding/base64
License:        Apache-2.0
URL:            https://github.com/cloudwego/base64x
#!RemoteAsset:  sha256:0a236c02dcb7c0e00b5ef1392d257e7b83b74325b3bfdf82d99d0f62f955d2e3
Source0:        https://github.com/cloudwego/base64x/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bytedance/sonic/loader)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/cloudwego/base64x) = %{version}

Requires:       go(github.com/bytedance/sonic/loader)
Requires:       go(github.com/klauspost/cpuid/v2)

%description
High-performance drop-in replacement for the Go encoding/base64 library.

%files
%doc README.md
%license LICENSE
%license LICENSE-APACHE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
