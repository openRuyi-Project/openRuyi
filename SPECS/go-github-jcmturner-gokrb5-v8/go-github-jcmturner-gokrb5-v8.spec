# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gokrb5
%define go_import_path  github.com/jcmturner/gokrb5/v8
# Client/integration tests need a live KDC, DNS SRV records, or Active Directory.
%define go_test_ignore_failure 1

Name:           go-github-jcmturner-gokrb5-v8
Version:        8.4.4
Release:        %autorelease
Summary:        Pure Go Kerberos v5 library
License:        Apache-2.0
URL:            https://github.com/jcmturner/gokrb5
#!RemoteAsset:  sha256:ddd7b1200d33a01cf9f129a4cfd122deb205cf9c10901a0c794dde1b56126a89
Source0:        https://github.com/jcmturner/gokrb5/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

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

Provides:       go(github.com/jcmturner/gokrb5/v8) = %{version}

Requires:       go(github.com/gorilla/sessions)
Requires:       go(github.com/hashicorp/go-uuid)
Requires:       go(github.com/jcmturner/aescts/v2)
Requires:       go(github.com/jcmturner/dnsutils/v2)
Requires:       go(github.com/jcmturner/gofork)
Requires:       go(github.com/jcmturner/goidentity/v6)
Requires:       go(github.com/jcmturner/rpc/v2)
Requires:       go(golang.org/x/crypto)

%description
gokrb5/v8 is a pure-Go Kerberos v5 implementation. IBM Sarama uses it
for optional Kafka GSSAPI authentication.

%prep -a
# Nested module github.com/jcmturner/gokrb5/v8; go.mod lives under v8/.
find . -maxdepth 1 -mindepth 1 -not -name v8 -not -name LICENSE -not -name NOTICE -not -name README.md -exec rm -rf {} +
cp -a v8/. .
rm -rf v8
# examples are sample programs, not the library.
rm -rf examples

%files
%doc README.md USAGE.md
%license LICENSE NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
