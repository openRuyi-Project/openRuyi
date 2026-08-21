# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dataset-go
%define go_import_path  github.com/scalyr/dataset-go

Name:           go-github-scalyr-dataset-go
Version:        0.21.0
Release:        %autorelease
Summary:        Go client for the DataSet API
License:        Apache-2.0
URL:            https://github.com/scalyr/dataset-go
#!RemoteAsset:  sha256:92e3aa3c8a74a8a49dd6558b35baddc8b69c7964c43c9b8b2da2097d81de4b5c
Source0:        https://github.com/scalyr/dataset-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/cenkalti/backoff/v4)
Requires:       go(github.com/google/uuid)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/exp)

%description
DataSet-Go is a Go client for sending structured and unstructured log events
through the DataSet addEvents API.

%files
%doc README.md RELEASE_NOTES.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
