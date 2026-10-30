# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gofmt
%define go_import_path  github.com/golangci/gofmt

Name:           go-github-golangci-gofmt
Version:        0+git20261022.e84e050
Release:        %autorelease
Summary:        Gofmt library adapter for Golangci-lint
License:        BSD-3-Clause
URL:            https://github.com/golangci/gofmt
#!RemoteAsset:  sha256:aa0d1fb7208cfcc916d66cca67d62c6225ba2bd3be54e66f1590e2ed82b5d578
Source0:        https://codeload.github.com/golangci/gofmt/tar.gz/e84e05053792206a61ddc23292559a6b1c4bfe40#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/rogpeppe/go-internal/diff)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sync/semaphore)
BuildRequires:  go(golang.org/x/tools)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/golangci/gofmt) = %{version}
Provides:       go(github.com/golangci/gofmt/internal) = %{version}
Provides:       go(github.com/golangci/gofmt/internal/internal/cfg) = %{version}
Provides:       go(github.com/golangci/gofmt/internal/internal/goarch) = %{version}
Provides:       go(github.com/golangci/gofmt/internal/internal/platform) = %{version}
Provides:       go(github.com/golangci/gofmt/internal/internal/testenv) = %{version}

Requires:       go(github.com/rogpeppe/go-internal/diff)
Requires:       go(golang.org/x/sync/semaphore)

%description
Gofmt library adapter for Golangci-lint. This package contains the complete
upstream repository sources and tests.

%prep
%autosetup -n gofmt-e84e05053792206a61ddc23292559a6b1c4bfe40

%files
%doc readme.md
%license internal/LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
