# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tracecontext.go
%define go_import_path  github.com/lightstep/tracecontext.go
%define commit_id       1757c391b1ac

Name:           go-github-lightstep-tracecontext.go
Version:        0+git20261023.1757c39
Release:        %autorelease
Summary:        Trace context header encoding for Go
License:        MIT
URL:            https://github.com/lightstep/tracecontext.go
#!RemoteAsset:  sha256:f55b607f8488434268271bb57ef56c772b3185fc64e761cd95f1f1311a31f36b
Source0:        https://github.com/lightstep/tracecontext.go/archive/%{commit_id}.tar.gz#/%{_name}-%{commit_id}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
# These tests use the original, unversioned Ginkgo and Gomega APIs.
BuildRequires:  go(github.com/onsi/ginkgo)
BuildRequires:  go(github.com/onsi/gomega)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/traceparent) = %{version}
Provides:       go(%{go_import_path}/tracestate) = %{version}

%description
tracecontext.go implements traceparent and tracestate header encoding,
decoding, and validation for propagating distributed trace context.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
