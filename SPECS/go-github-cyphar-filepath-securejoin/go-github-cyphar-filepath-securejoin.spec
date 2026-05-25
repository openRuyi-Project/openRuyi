# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           filepath-securejoin
%define go_import_path  github.com/cyphar/filepath-securejoin

Name:           go-github-cyphar-filepath-securejoin
Version:        0.6.1
Release:        %autorelease
Summary:        Proposed filepath.SecureJoin implementation
License:        BSD-3-Clause AND MPL-2.0
URL:            https://github.com/cyphar/filepath-securejoin
#!RemoteAsset:  sha256:3afa713f591b60e27e27e053e4ceba5c78657fbcf7bd1afc33f54436409a0f2e
Source0:        https://github.com/cyphar/filepath-securejoin/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n filepath-securejoin-0.6.1
# OBS returns "resource temporarily unavailable" for several openat2 symlink
# loop cases, and the racing mkdir stress test hits "too many open files" on
# riscv64. TestPartialLookup_RacingRename also exceeds the 10m go test timeout
# on riscv64 workers. Keep the rest of upstream tests enabled.
BuildOption(check):  -skip 'TestMkdirAllHandle_Basic|TestMkdirAllHandle_RacingCreate|TestOpenInRoot|TestPartialLookup_RacingRename'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/unix)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/cyphar/filepath-securejoin) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/internal/consts) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/internal/testutils) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/pathrs-lite) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/pathrs-lite/internal) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/pathrs-lite/internal/assert) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/pathrs-lite/internal/fd) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/pathrs-lite/internal/gocompat) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/pathrs-lite/internal/gopathrs) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/pathrs-lite/internal/kernelversion) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/pathrs-lite/internal/linux) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/pathrs-lite/internal/procfs) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/pathrs-lite/internal/testutils) = %{version}
Provides:       go(github.com/cyphar/filepath-securejoin/pathrs-lite/procfs) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/stretchr/testify/assert)
Requires:       go(github.com/stretchr/testify/require)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/sys/unix)
Requires:       go(gopkg.in/yaml.v3)


%description
filepath-securejoin

[Image: Go Documentation]
(https://pkg.go.dev/badge/github.com/cyphar/filepath-securejoin.svg)
(https://pkg.go.dev/github.com/cyphar/filepath-securejoin) [Image: Build
Status] (https://github.com/cyphar/filepath-
securejoin/actions/workflows/ci.yml/badge.svg)
(https://github.com/cyphar/filepath-securejoin/actions/workflows/ci.yml)

Old API


%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE.BSD
%license LICENSE.MPL-2.0
%license COPYING.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
