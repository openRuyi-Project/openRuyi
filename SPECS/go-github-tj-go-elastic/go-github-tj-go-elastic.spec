# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-elastic
%define go_import_path  github.com/tj/go-elastic
# TestClient_* requires a live Elasticsearch ES_ADDR; without it the request
# fails with Post "/_refresh": unsupported protocol scheme "".
%global go_test_flags_default -v -skip '^TestClient_'
%global commit_id       36157cbbebc210c55c1c8a82c8655ccbb9f41aa0

Name:           go-github-tj-go-elastic
Version:        0+git20261020.36157cb
Release:        %autorelease
Summary:        Elasticsearch client with AWS request signing
License:        MIT
URL:            https://github.com/tj/go-elastic
#!RemoteAsset:  sha256:bb485541e07783859e3f2e5103938f1bdffbbf9cb8f902628304ddc141550684
Source0:        https://github.com/tj/go-elastic/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Map iteration made alias-removal JSON and its exact-output test nondeterministic.
Patch2000:      2000-sort-index-removal-actions.patch

BuildOption(prep):  -n go-elastic-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/apex/log)
BuildRequires:  go(github.com/smartystreets/go-aws-auth)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/tj/go-elastic) = %{version}

Requires:       go(github.com/smartystreets/go-aws-auth)

%description
This package provides an Elasticsearch client with AWS Signature
Version 4 support and batched indexing.

%files
%doc Readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
