# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mint
%define go_import_path  github.com/otiai10/mint

Name:           go-github-otiai10-mint
Version:        1.6.3
Release:        %autorelease
Summary:        Minimal assertion library for Go tests
License:        MIT
URL:            https://github.com/otiai10/mint
#!RemoteAsset:  sha256:b02c8a525922a7eb63f03ef8a3223f4a167d7454b7c3df722f1901fadbe07b5b
Source0:        https://github.com/otiai10/mint/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.27 vet rejects the upstream examples' legacy test signatures.
BuildOption(check):  -vet=off

BuildRequires:  go >= 1.18
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/curr) = %{version}
Provides:       go(%{go_import_path}/mquery) = %{version}

%description
A minimal assertion library for Go tests, with helpers for matching,
querying, and inspecting values.

# curr tests compare paths against the single source root, while the default
# check runs with a multi-entry GOPATH.
%check -p
export GITHUB_WORKSPACE="%{_builddir}/go/src/%{go_import_path}"

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
