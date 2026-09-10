# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ansiterm
%define go_import_path  github.com/Azure/go-ansiterm
%define commit_id       faa5f7b0171c46bb398a91b4a0c906324d3664cf

Name:           go-github-azure-go-ansiterm
Version:        0+git20260818.faa5f7b
Release:        %autorelease
Summary:        ANSI terminal emulation library for Go
License:        MIT
URL:            https://github.com/Azure/go-ansiterm
#!RemoteAsset:  sha256:17e7f56d4f981022a7bb5bbf5b2385d73aa57dcbcfb7f3ce3cf80228ec557cbe
Source0:        https://github.com/Azure/go-ansiterm/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Call the state name method when logging a failed transition.
Patch2000:      2000-Fix-logging-of-transition-target-state.patch

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/sys)

%description
Go ANSI terminal provides a parser and terminal implementation used to process
ANSI escape sequences, including Windows console support.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
