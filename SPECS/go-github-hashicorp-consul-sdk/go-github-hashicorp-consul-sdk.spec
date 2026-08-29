# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           consul
%define go_import_path  github.com/hashicorp/consul/sdk
%define archive_dir     consul-sdk-v%{version}

# Some sdk helpers (testutil/retry) start local servers and probe the network,
# which the isolated build sandbox restricts; run the tests but tolerate them.
%global go_test_ignore_failure 1

Name:           go-github-hashicorp-consul-sdk
Version:        0.18.1
Release:        %autorelease
Summary:        Shared SDK helpers for HashiCorp Consul
License:        MPL-2.0
URL:            https://github.com/hashicorp/consul
#!RemoteAsset:  sha256:a3827a453ca0e255482cb31076c6c293e9a286a08ab893d651c4966bdca1b67f
Source0:        https://github.com/hashicorp/consul/archive/refs/tags/sdk/v%{version}.tar.gz#/%{_name}-sdk-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{archive_dir}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-uuid)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/hashicorp/consul/sdk) = %{version}

Requires:       go(github.com/hashicorp/go-cleanhttp)
Requires:       go(github.com/hashicorp/go-hclog)
Requires:       go(github.com/hashicorp/go-uuid)
Requires:       go(github.com/hashicorp/go-version)
Requires:       go(github.com/pkg/errors)

# The upstream archive is the whole consul repository; keep only the sdk
# submodule so the build targets github.com/hashicorp/consul/sdk alone.
%prep -a
find . -maxdepth 1 -mindepth 1 -not -name sdk -exec rm -rf {} +
shopt -s dotglob
mv sdk/* .
rmdir sdk

%description
This package provides the shared SDK helpers (github.com/hashicorp/consul/sdk)
used by the HashiCorp Consul API client and tests.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
