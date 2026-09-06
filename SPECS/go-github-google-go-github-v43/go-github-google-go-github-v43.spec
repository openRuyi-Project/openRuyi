# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-github
%define go_import_path  github.com/google/go-github/v43

Name:           go-github-google-go-github-v43
Version:        43.0.0
Release:        %autorelease
Summary:        Go client library for the GitHub API
License:        BSD-3-Clause
URL:            https://github.com/google/go-github
#!RemoteAsset:  sha256:78baf73614ebefd56f822c7c9a0d60793c561acca9402e8d2a2d18190b905cba
Source0:        https://github.com/google/go-github/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use the bundled v43 root module for the bundled scrape module.
Patch2000:      2000-Use-bundled-root-module-in-scrape-package.patch
# Fix a non-constant format string rejected by current Go vet.
Patch2001:      2001-Fix-non-constant-update-urls-test-format-string.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/GoKillers/libsodium-go)
BuildRequires:  go(github.com/PuerkitoBio/goquery)
BuildRequires:  go(github.com/bradleyfalzon/ghinstallation/v2)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-querystring)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/xlzd/gotp)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(google.golang.org/appengine)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/bradleyfalzon/ghinstallation/v2)
Requires:       go(github.com/GoKillers/libsodium-go)
Requires:       go(github.com/PuerkitoBio/goquery)
Requires:       go(github.com/google/go-querystring)
Requires:       go(github.com/xlzd/gotp)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(google.golang.org/appengine)

%description
Go-github provides a Go client library for accessing the GitHub REST API.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
