# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-retryablehttp
%define go_import_path  github.com/hashicorp/go-retryablehttp

Name:           go-github-hashicorp-go-retryablehttp
Version:        0.7.8
Release:        %autorelease
Summary:        Retryable HTTP client in Go
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-retryablehttp
#!RemoteAsset:  sha256:a556692913b852c228fbfca680bb6660bc851485155dd2c1c5f4017497398823
Source0:        https://github.com/hashicorp/go-retryablehttp/archive/refs/tags/v0.7.8.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-retryablehttp-0.7.8

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/hashicorp/go-retryablehttp) = %{version}

Requires:       go(github.com/hashicorp/go-cleanhttp)


%description
go-retryablehttp

[Image: Build Status] (http://img.shields.io/travis/hashicorp/go-
retryablehttp.svg?style=flat-square) (http://travis-ci.org/hashicorp/go-
retryablehttp) [Image: Go Documentation] (http://img.shields.io/badge/go-
documentation-blue.svg?style=flat-square)
(http://godoc.org/github.com/hashicorp/go-retryablehttp)

The retryablehttp package provides a familiar HTTP client interface with
automatic retries and exponential backoff. It is a thin wrapper over the
standard net/http client library and exposes nearly the same public API.

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
