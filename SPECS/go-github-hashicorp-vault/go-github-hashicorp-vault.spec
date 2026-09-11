# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           vault
%define go_import_path  github.com/hashicorp/vault/api

# Vault's API is an independently tagged MPL-2.0 module in the monorepo.
Name:           go-github-hashicorp-vault
Version:        1.14.0
Release:        %autorelease
Summary:        Go API client for HashiCorp Vault
License:        MPL-2.0
URL:            https://github.com/hashicorp/vault
#!RemoteAsset:  sha256:c652e3a6f43f6886e91f7e6889d0fcfc1a3377c77ce23ac78c27d9f2718f82d4
Source0:        https://github.com/hashicorp/vault/archive/refs/tags/api/v%{version}.tar.gz#/%{_name}-api-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Backport the API error fix from https://github.com/hashicorp/vault/pull/29412.
Patch1000:      1000-backport-parse-secret-error-fix.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cenkalti/backoff/v3)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/go-test/deep)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)
BuildRequires:  go(github.com/hashicorp/go-rootcerts)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/parseutil)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/strutil)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/natefinch/atomic)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/time)

Provides:       go(github.com/hashicorp/vault/api) = %{version}
Provides:       go(github.com/hashicorp/vault/api/cliconfig) = %{version}
Provides:       go(github.com/hashicorp/vault/api/tokenhelper) = %{version}

Requires:       go(github.com/cenkalti/backoff/v3)
Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(github.com/hashicorp/errwrap)
Requires:       go(github.com/hashicorp/go-cleanhttp)
Requires:       go(github.com/hashicorp/go-multierror)
Requires:       go(github.com/hashicorp/go-retryablehttp)
Requires:       go(github.com/hashicorp/go-rootcerts)
Requires:       go(github.com/hashicorp/go-secure-stdlib/parseutil)
Requires:       go(github.com/hashicorp/go-secure-stdlib/strutil)
Requires:       go(github.com/hashicorp/hcl)
Requires:       go(github.com/mitchellh/go-homedir)
Requires:       go(github.com/mitchellh/mapstructure)
Requires:       go(github.com/natefinch/atomic)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/time)

%description
The Vault API module provides a Go client for authentication, secrets,
leases and administrative endpoints, including its public helper packages.
This package contains the reusable MPL-2.0 API module.

%prep -a
# Keep the complete API module, not the separately licensed Vault server.
find . -mindepth 1 -maxdepth 1 ! -name api -exec rm -rf {} +
shopt -s dotglob
mv api/* .
rmdir api
# auth/* are separately versioned adapter modules, not API subpackages.
rm -rf auth

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
