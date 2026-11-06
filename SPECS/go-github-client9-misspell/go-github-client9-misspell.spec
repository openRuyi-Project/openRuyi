# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           misspell
%define go_import_path  github.com/client9/misspell

Name:           go-github-client9-misspell
Version:        0.3.4
Release:        %autorelease
Summary:        English spelling correction library and tool for Go
License:        MIT
URL:            https://github.com/client9/misspell
#!RemoteAsset:  sha256:4bbb94da9bf4500fef21f83359c61c92429a13b47b064bd62fedb68c62b66001
Source0:        https://github.com/client9/misspell/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects the redundant newline from fmt.Println.
Patch2000:       2000-fix-vet-redundant-newline.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gobwas/glob)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/client9/misspell) = %{version}
Provides:       go(github.com/client9/misspell/cmd/misspell) = %{version}
Provides:       go(github.com/client9/misspell/ignore) = %{version}

Requires:       go(github.com/gobwas/glob)

%description
English spelling correction library and tool for Go. This package contains
the complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
