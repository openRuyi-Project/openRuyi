# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-amqp
%define go_import_path  github.com/Azure/go-amqp

Name:           go-github-azure-go-amqp
Version:        1.7.0
Release:        %autorelease
Summary:        AMQP 1.0 client for Go
License:        MIT
URL:            https://github.com/Azure/go-amqp
#!RemoteAsset:  sha256:215c3a84712b92519abd3e31fbcc9ee10fd8812cc86b1cb9249d620ea78d6693
Source0:        https://github.com/Azure/go-amqp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.25
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fortytw2/leaktest)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/internal/bitmap) = %{version}
Provides:       go(%{go_import_path}/internal/buffer) = %{version}
Provides:       go(%{go_import_path}/internal/debug) = %{version}
Provides:       go(%{go_import_path}/internal/encoding) = %{version}
Provides:       go(%{go_import_path}/internal/fake) = %{version}
Provides:       go(%{go_import_path}/internal/frames) = %{version}
Provides:       go(%{go_import_path}/internal/queue) = %{version}
Provides:       go(%{go_import_path}/internal/shared) = %{version}
Provides:       go(%{go_import_path}/internal/test) = %{version}
Provides:       go(%{go_import_path}/internal/testconn) = %{version}

Requires:       go(github.com/google/go-cmp)

%description
go-amqp implements an AMQP 1.0 client with connections, sessions,
senders, receivers, and message settlement support.

%files
%doc README.md
%license LICENSE NOTICE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
