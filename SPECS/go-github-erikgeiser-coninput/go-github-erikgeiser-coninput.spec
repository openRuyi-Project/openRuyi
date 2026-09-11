# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           coninput
%define go_import_path  github.com/erikgeiser/coninput
%define commit_id       1c3628e74d0f39ad7e963960ab9799c7f6ca3761
# Linux has no Console API; go test is empty.
%define go_test_ignore_failure 1

Name:           go-github-erikgeiser-coninput
Version:        0+git20260907.1c3628e
Release:        %autorelease
Summary:        Windows Console API input handling for Go
License:        MIT
URL:            https://github.com/erikgeiser/coninput
#!RemoteAsset:  sha256:229766b58e5a1e0a863f765a5341847d012adfa9df12a52d60aba763912bb5f7
Source0:        https://github.com/erikgeiser/coninput/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/erikgeiser/coninput) = %{version}

Requires:       go(golang.org/x/sys)

%description
coninput reads input events through the Windows Console API. Linux
has no packages to test.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
