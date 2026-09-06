# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-secure-stdlib
%define go_import_path  github.com/hashicorp/go-secure-stdlib
%define ver_parseutil   0.2.0
%define ver_strutil     0.1.2
%define ver_awsutil     0.3.0
%define dir_parseutil   go-secure-stdlib-parseutil-v%{ver_parseutil}
%define dir_awsutil     go-secure-stdlib-awsutil-v%{ver_awsutil}
# Go 1.26 rejects invalid IP literals that the old parseutil tests accept.
%define go_test_exclude %{go_import_path}/parseutil

Name:           go-github-hashicorp-go-secure-stdlib
Version:        0.3.0
Release:        %autorelease
Summary:        Security utility modules for HashiCorp Go projects
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-secure-stdlib
#!RemoteAsset:  sha256:b5496b263f0b94972f4aac96a3f09243cd9e9591b6361c25969a3cbe5f6f8428
Source0:        https://github.com/hashicorp/go-secure-stdlib/archive/refs/tags/parseutil/v%{ver_parseutil}.tar.gz#/%{_name}-parseutil-%{ver_parseutil}.tar.gz
#!RemoteAsset:  sha256:0e476be20601d2fb8383f65dd28a4bd69cf53d536cc442f88a27a3fb3f9cd77b
Source1:        https://github.com/hashicorp/go-secure-stdlib/archive/refs/tags/awsutil/v%{ver_awsutil}.tar.gz#/%{_name}-awsutil-%{ver_awsutil}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/aws-sdk-go)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/go-sockaddr)
BuildRequires:  go(github.com/jmespath/go-jmespath)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/ryanuber/go-glob)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}/awsutil) = %{ver_awsutil}
Provides:       go(%{go_import_path}/parseutil) = %{ver_parseutil}
Provides:       go(%{go_import_path}/strutil) = %{ver_strutil}

Requires:       go(github.com/aws/aws-sdk-go)
Requires:       go(github.com/hashicorp/errwrap)
Requires:       go(github.com/hashicorp/go-cleanhttp)
Requires:       go(github.com/hashicorp/go-hclog)
Requires:       go(github.com/hashicorp/go-multierror)
Requires:       go(github.com/hashicorp/go-sockaddr)
Requires:       go(github.com/mitchellh/mapstructure)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/ryanuber/go-glob)

%description
This package bundles the awsutil, parseutil, and strutil modules from
HashiCorp's Go security utility repository.

%prep
%setup -q -c -T -a 0
%setup -q -D -T -a 1

%install
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}"
cp -a "%{dir_parseutil}/parseutil" "%{dir_parseutil}/strutil" \
    "%{buildroot}%{go_sys_gopath}/%{go_import_path}/"
cp -a "%{dir_awsutil}/awsutil" \
    "%{buildroot}%{go_sys_gopath}/%{go_import_path}/"

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
install -d "%{_builddir}/go/src/%{go_import_path}"
cp -a "%{buildroot}%{go_sys_gopath}/%{go_import_path}/." \
    "%{_builddir}/go/src/%{go_import_path}/"
pushd "%{_builddir}/go/src/%{go_import_path}/parseutil"
go test -run '^$' $(go list -e -f '{{.ImportPath}}' ./...)
popd
pushd "%{_builddir}/go/src/%{go_import_path}/strutil"
go test -v $(go list -e -f '{{.ImportPath}}' ./...)
popd
pushd "%{_builddir}/go/src/%{go_import_path}/awsutil"
go test -v $(go list -e -f '{{.ImportPath}}' ./...)
popd

%files
%doc %{dir_parseutil}/README.md
%license %{dir_parseutil}/LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
