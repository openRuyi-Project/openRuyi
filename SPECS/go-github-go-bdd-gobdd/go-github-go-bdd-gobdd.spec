# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gobdd
%define go_import_path  github.com/go-bdd/gobdd
%define commit          ca566a78d07579daa65f58b1053a7f5f67b8b8e7

Name:           go-github-go-bdd-gobdd
Version:        1.1.3+git20260817.ca566a7
Release:        %autorelease
Summary:        Behavior-driven testing framework for Go
License:        MIT
URL:            https://github.com/go-bdd/gobdd
#!RemoteAsset:  sha256:36a05cbb8789b47d0cad62b8cfde3847c12d3688e679467bb2904baead86eb28
Source0:        https://github.com/go-bdd/gobdd/archive/%{commit}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/go-bdd/gobdd/commit/de7b6339a33ed28fa8733acfcff1aab60409d574
Patch1:         1000-use-supported-format-verbs-in-Errorf-calls.patch

BuildOption(prep):  -n %{_name}-%{commit}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cucumber/gherkin-go/v13)
BuildRequires:  go(github.com/cucumber/messages-go/v12)
BuildRequires:  go(github.com/go-bdd/assert)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/cucumber/gherkin-go/v13)
Requires:       go(github.com/cucumber/messages-go/v12)
Requires:       go(github.com/go-bdd/assert)

%description
Gobdd runs Gherkin behavior specifications through Go's native testing
framework, preserving normal debugging and test tooling.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
