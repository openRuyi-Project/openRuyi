# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           redis
%define go_import_path  github.com/gomodule/redigo
%define commit_id 57c8b99ccb90c3401bec6e09289081e8b78b3bde

Name:           go-github-gomodule-redigo-redis
Version:        0+git20251102.57c8b99
Release:        %autorelease
Summary:        Redis client library for Go
License:        Apache-2.0
URL:            https://github.com/gomodule/redigo
#!RemoteAsset:  sha256:989b89b14c2652a8f30fbd3037ff58f4f76cdb6a196445718a033853712c4509
Source0:        https://github.com/gomodule/redigo/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# redisx tests and redis examples/TestScript require redis-server, which is not
# packaged; keep the redis unit tests that do not start an external server.
%define go_test_exclude github.com/gomodule/redigo/redisx
BuildOption(check):  -vet=off -run '^(TestLookupCommandInfo|TestWrite|TestRead|TestReadString|TestDialURLErrors|TestDialURLPort|TestDialURLHost|TestDialURL|TestDialUseTLS|TestDialTLSHandshakeTimeout|TestDialTLSSKipVerify|TestDialUseACL|TestWithTimeout|TestPoolGetContext_DialContext|TestWaitPoolGetAfterClose|TestWaitPoolGetCanceledContext|TestConnTimeout|TestPoolConnTimeout|TestConnContext|TestPoolConnContext|TestReply|TestScan.*|TestArgs)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/gomodule/redigo/redis) = %{version}
Provides:       go(github.com/gomodule/redigo/redisx) = %{version}


%description
This package provides the Redigo Redis client library for Go.

%files
%doc README.markdown
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
