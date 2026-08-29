# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           consul
%define go_import_path  github.com/hashicorp/consul/api
%define archive_dir     consul-api-v%{version}

# Some api tests start a local Consul agent / probe the network, which the
# isolated build sandbox restricts; run the tests but tolerate the failures.
%global go_test_ignore_failure 1

Name:           go-github-hashicorp-consul-api
Version:        1.32.1
Release:        %autorelease
Summary:        Go client library for the HashiCorp Consul HTTP API
License:        MPL-2.0
URL:            https://github.com/hashicorp/consul
#!RemoteAsset:  sha256:ed118767ca37e3caf003b0a2e7e1b0b3b335590950d8f278833bf1cde6b9dc08
Source0:        https://github.com/hashicorp/consul/archive/refs/tags/api/v%{version}.tar.gz#/%{_name}-api-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{archive_dir}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/hashicorp/consul/sdk)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/go-rootcerts)
BuildRequires:  go(github.com/hashicorp/go-uuid)
BuildRequires:  go(github.com/hashicorp/serf)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/exp)

Provides:       go(github.com/hashicorp/consul/api) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/hashicorp/consul/sdk)
Requires:       go(github.com/hashicorp/go-cleanhttp)
Requires:       go(github.com/hashicorp/go-hclog)
Requires:       go(github.com/hashicorp/go-multierror)
Requires:       go(github.com/hashicorp/go-rootcerts)
Requires:       go(github.com/hashicorp/go-uuid)
Requires:       go(github.com/hashicorp/serf)
Requires:       go(github.com/mitchellh/mapstructure)

# The upstream archive is the whole consul repository; keep only the api
# submodule so the build targets github.com/hashicorp/consul/api alone.
%prep -a
find . -maxdepth 1 -mindepth 1 -not -name api -exec rm -rf {} +
shopt -s dotglob
mv api/* .
rmdir api
# Drop the local replace directive so the packaged consul/sdk is used.
sed -i '\#replace github.com/hashicorp/consul/sdk#d' go.mod

%description
This package provides the Go client library (github.com/hashicorp/consul/api)
for interacting with the HashiCorp Consul HTTP API, used by Prometheus' Consul
service discovery.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
