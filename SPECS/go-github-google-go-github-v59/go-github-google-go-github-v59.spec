# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-github
%define go_import_path  github.com/google/go-github/v59
# Nested Go modules have their own module path/dependencies; skip them in
# %check so the parent package does not try to test unrelated internal tools.
# - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/example*
    %{go_import_path}/scrape*
    %{go_import_path}/tools*
}

Name:           go-github-google-go-github-v59
Version:        59.0.0
Release:        %autorelease
Summary:        Go client library for the GitHub API
License:        BSD-3-Clause
URL:            https://github.com/google/go-github
#!RemoteAsset:  sha256:30860bb4e4e8e532519f12d8c44689100f12b03d20ed0e4358269f5a54644d4e
Source0:        https://github.com/google/go-github/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Some build environments map .txt to the generic application/octet-stream MIME
# type; sniff named assets before falling back to the default upload type.
# - HNO3Miracle
Patch2000:      2000-detect-generic-release-asset-content-types.patch

# Go 1.26 vet reports Errorf %q with a *strings.Reader argument in upstream
# github tests; keep tests enabled but disable vet. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-querystring)

Provides:       go(github.com/google/go-github/v59) = %{version}

Requires:       go(github.com/google/go-querystring)

%description
go-github is a Go client library for accessing the GitHub REST API.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
# Nested Go modules are packaged separately; do not let this module own
# their source directories, otherwise RPM can hit file conflicts.
%exclude %{go_sys_gopath}/%{go_import_path}/example
%exclude %{go_sys_gopath}/%{go_import_path}/scrape
%exclude %{go_sys_gopath}/%{go_import_path}/tools

%changelog
%autochangelog
