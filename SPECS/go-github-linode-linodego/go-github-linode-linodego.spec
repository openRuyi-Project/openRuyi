# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           linodego
%define go_import_path  github.com/linode/linodego
# Upstream integration tests require a real LINODE_TOKEN cloud credential.
%global go_test_exclude_glob %{shrink:
%{go_import_path}/test/integration*
%{go_import_path}/test/unit*
}

Name:           go-github-linode-linodego
Version:        1.66.0
Release:        %autorelease
Summary:        Go client for the Linode REST v4 API
License:        MIT
URL:            https://github.com/linode/linodego
#!RemoteAsset:  sha256:5494525d4042a3a1541e133044267e1993242484abefdf22f8d11316a5745c1a
Source0:        https://github.com/linode/linodego/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/dnaeon/go-vcr/cassette)
BuildRequires:  go(github.com/dnaeon/go-vcr/recorder)
BuildRequires:  go(github.com/go-resty/resty/v2)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-querystring)
BuildRequires:  go(github.com/jarcoal/httpmock)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/ini.v1)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/client-go)

Provides:       go(github.com/linode/linodego) = %{version}

Requires:       go(github.com/dnaeon/go-vcr/cassette)
Requires:       go(github.com/dnaeon/go-vcr/recorder)
Requires:       go(github.com/go-resty/resty/v2)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-querystring)
Requires:       go(github.com/jarcoal/httpmock)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/text)
Requires:       go(gopkg.in/ini.v1)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/client-go)

%description
Linodego is the Go client library for the Linode REST v4 API. It provides
typed APIs for working with Linode cloud resources from Go programs.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
