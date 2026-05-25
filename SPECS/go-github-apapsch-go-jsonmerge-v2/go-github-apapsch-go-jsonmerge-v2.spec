# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-jsonmerge
%define go_import_path  github.com/apapsch/go-jsonmerge/v2

Name:           go-github-apapsch-go-jsonmerge-v2
Version:        2.0.0
Release:        %autorelease
Summary:        Merge JSON objects
License:        MIT
URL:            https://github.com/apapsch/go-jsonmerge
#!RemoteAsset:  sha256:617f4e0c2029a2e6858a56c5fb2f8e6637cfdab42e4cfbfc8d2b95899fdee6fd
Source0:        https://github.com/apapsch/go-jsonmerge/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The v2.0.0 CLI sources still use the pre-v2 module path and old API.
# Patch them to the canonical v2 module API so %check can build the CLI package.
# - HNO3Miracle
Patch2000:      2000-fix-v2-cli-api-usage.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/apapsch/go-jsoncommentstrip)
BuildRequires:  go(github.com/bmatcuk/doublestar)
BuildRequires:  go(github.com/juju/gnuflag)
BuildRequires:  go(github.com/spkg/bom)

Provides:       go(github.com/apapsch/go-jsonmerge/v2) = %{version}

Requires:       go(github.com/apapsch/go-jsoncommentstrip)
Requires:       go(github.com/bmatcuk/doublestar)
Requires:       go(github.com/juju/gnuflag)
Requires:       go(github.com/spkg/bom)

%description
go-jsonmerge provides a Go library and command-line helper for merging JSON
objects.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
