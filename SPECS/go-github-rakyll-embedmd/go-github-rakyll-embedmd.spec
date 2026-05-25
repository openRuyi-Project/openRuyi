# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           embedmd
%define go_import_path  github.com/rakyll/embedmd
# The root package integration test executes the embedmd binary, which is not
# built by this library package. The embedmd subpackage also asserts the old
# net/url parse error formatting changed by Go 1.25. - HNO3Miracle
%define go_test_exclude %{shrink:
    github.com/rakyll/embedmd
    github.com/rakyll/embedmd/embedmd
}

Name:           go-github-rakyll-embedmd
Version:        0.1
Release:        %autorelease
Summary:        Markdown embedding tool for Go
License:        Apache-2.0
URL:            https://github.com/rakyll/embedmd
#!RemoteAsset:  sha256:12bc0aa0ff9c0af26685382ee3af3570f8f32435ca8cdd010a0aef2e956f82de
Source0:        https://github.com/rakyll/embedmd/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/campoy/embedmd/embedmd)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/rakyll/embedmd) = %{version}

Requires:       go(github.com/campoy/embedmd/embedmd)
Requires:       go(github.com/pmezard/go-difflib)

%description
embedmd embeds files or command output into Markdown documents.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
