# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tools
%define go_import_path  honnef.co/go/tools
%define upstream_version  0.7.0-0.dev

Name:           go-honnef-go-tools
Version:        0.7.0~0.dev
Release:        %autorelease
Summary:        Staticcheck tools for Go
License:        MIT
URL:            https://github.com/dominikh/go-tools
#!RemoteAsset:  sha256:0a3fa9aa78b18c225edf5984caffd782a78dc49667372c9985c21fd3901e088a
Source0:        https://github.com/dominikh/go-tools/archive/refs/tags/v%{upstream_version}.tar.gz#/%{_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet reports fmt.Sprintf %q with an int64 argument in
# staticcheck/sa1030; keep tests enabled but disable vet. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go-golang-x-tools-go-expect
BuildRequires:  go-rpm-macros

Provides:       go(honnef.co/go/tools) = %{version}

Requires:       go(github.com/BurntSushi/toml)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/tools/go/expect)

%description
This package provides Staticcheck tools and supporting libraries for Go.

%files
%doc README.md
%license LICENSE
%license LICENSE-THIRD-PARTY
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
