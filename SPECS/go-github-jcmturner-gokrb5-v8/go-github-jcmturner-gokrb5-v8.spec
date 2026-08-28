# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name            gokrb5
%define go_import_path   github.com/jcmturner/gokrb5/v8

Name:           go-github-jcmturner-gokrb5-v8
Version:        8.4.4
Release:        %autorelease
Summary:        Pure Go implementation of Kerberos
License:        Apache-2.0
URL:            https://github.com/jcmturner/gokrb5
#!RemoteAsset:  sha256:ddd7b1200d33a01cf9f129a4cfd122deb205cf9c10901a0c794dde1b56126a89
Source0:        https://github.com/jcmturner/gokrb5/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix a Go 1.26 vet error caused by a dynamic fmt.Errorf format.
# https://github.com/jcmturner/gokrb5/pull/579
Patch0:         2000-client-fix-non-constant-fmt.Errorf-format.patch

# Keep the replay-cache test serialized to avoid parallel test interference.
Patch1:         2001-service-avoid-running-replay-test-in-parallel.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gorilla/sessions)
BuildRequires:  go(github.com/hashicorp/go-uuid)
BuildRequires:  go(github.com/jcmturner/aescts/v2)
BuildRequires:  go(github.com/jcmturner/dnsutils/v2)
BuildRequires:  go(github.com/jcmturner/gofork)
BuildRequires:  go(github.com/jcmturner/goidentity/v6)
BuildRequires:  go(github.com/jcmturner/rpc/v2)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/jcmturner/gokrb5/v8) = %{version}

Requires:       go(github.com/gorilla/sessions)
Requires:       go(github.com/hashicorp/go-uuid)
Requires:       go(github.com/jcmturner/aescts/v2)
Requires:       go(github.com/jcmturner/dnsutils/v2)
Requires:       go(github.com/jcmturner/gofork)
Requires:       go(github.com/jcmturner/goidentity/v6)
Requires:       go(github.com/jcmturner/rpc/v2)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)

%description
Gokrb5 provides a pure Go implementation of the Kerberos authentication
protocol for client, server, and custom integration use cases.

%install
pushd v8
%buildsystem_golangmodules_install
popd

%check
pushd v8
%buildsystem_golangmodules_check
popd

%files
%doc NOTICE README.md USAGE.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
