# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           yunion-executor
%define go_import_path  yunion.io/x/executor
%define commit_id       5402e9e0bed0c88971c881da0fec982a9bf1234f

Name:           yunion-executor
Version:        0+git20260922.5402e9e
Release:        %autorelease
Summary:        Remote command execution over gRPC
License:        Apache-2.0
URL:            https://github.com/yunionio/executor
#!RemoteAsset:  sha256:82bc4f96a8344030dafb4cdd60ed5d3a36004e3a6ad51bb3c5791d2131dba6af
Source0:        https://github.com/yunionio/executor/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(yunion.io/x/log)
BuildRequires:  go(yunion.io/x/pkg/util/signalutils)
BuildRequires:  go(yunion.io/x/pkg/utils)

%package     -n go-yunion-x-executor
Summary:        Go client and server libraries for the Yunion executor
BuildArch:      noarch

Provides:       go(yunion.io/x/executor) = %{version}

Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/pkg/errors)
Requires:       go(google.golang.org/grpc)
Requires:       go(yunion.io/x/log)
Requires:       go(yunion.io/x/pkg/util/signalutils)
Requires:       go(yunion.io/x/pkg/utils)

%description
The Yunion executor runs commands over gRPC using a Unix socket. It can
operate as a server or as an interactive command-line client.

%description -n go-yunion-x-executor
This package provides the reusable client, server and protocol sources
for Yunion's remote command executor.

%prep -a
# The Go prep stage also copies the source into GOPATH.
rm -rf vendor %{_builddir}/go/src/%{go_import_path}/vendor

%install -a
rm -f %{_name}
%buildsystem_golangmodules_install

%check -a
%{buildroot}%{_bindir}/%{_name} -h 2>&1 | grep -F -- '-socket-path'

%files
%doc README.md
%license LICENSE
%{_bindir}/%{_name}

%files -n go-yunion-x-executor
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
