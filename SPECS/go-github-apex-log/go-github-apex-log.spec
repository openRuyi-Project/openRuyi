# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           log
%define go_import_path  github.com/apex/log
# These handlers require clients that import the logging core.
# Defer their compilation checks until the client packages are available.
%define go_test_exclude %{shrink:
    %{go_import_path}/handlers/es
    %{go_import_path}/handlers/kinesis
}

Name:           go-github-apex-log
Version:        1.9.0
Release:        %autorelease
Summary:        Structured logging API and common handlers for Go
License:        MIT
URL:            https://github.com/apex/log
#!RemoteAsset:  sha256:6171253fb8b022d5151a5b4b9847bcd6f2cdc2fd7180a741090626d73d311890
Source0:        https://github.com/apex/log/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n log-%{version}

# Go vet rejects the upstream example: Example_trace should return nothing.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/apex/logs)
BuildRequires:  go(github.com/aphistic/golf)
BuildRequires:  go(github.com/aybabtme/rgbterm)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/go-logfmt/logfmt)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tj/assert)
BuildRequires:  go(github.com/tj/go-buffer)
BuildRequires:  go(github.com/tj/go-spin)

Provides:       go(github.com/apex/log) = %{version}

Requires:       go(github.com/apex/logs)
Requires:       go(github.com/aphistic/golf)
Requires:       go(github.com/aybabtme/rgbterm)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/go-logfmt/logfmt)
Requires:       go(github.com/mattn/go-colorable)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/tj/go-buffer)
Requires:       go(github.com/tj/go-spin)

%description
Apex Log provides a structured logging API with pluggable handlers for
terminals, JSON, GELF, and Apex Logs. Elasticsearch and Amazon Kinesis
handlers are available as separate packages.

%package        handlers-es
Summary:        Elasticsearch handler for Apex Log

Provides:       go(%{go_import_path}/handlers/es) = %{version}

Requires:       go(%{go_import_path})
Requires:       go(github.com/tj/go-elastic)

%description    handlers-es
This package provides the Elasticsearch batch handler for Apex Log.

%package        handlers-kinesis
Summary:        Amazon Kinesis handler for Apex Log

Provides:       go(%{go_import_path}/handlers/kinesis) = %{version}

Requires:       go(%{go_import_path})
Requires:       go(github.com/aws/aws-sdk-go)
Requires:       go(github.com/rogpeppe/fastuuid)
Requires:       go(github.com/tj/go-kinesis)

%description    handlers-kinesis
This package provides the Amazon Kinesis handler for Apex Log.

%files
%doc Readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/handlers/es
%exclude %{go_sys_gopath}/%{go_import_path}/handlers/kinesis

%files handlers-es
%doc Readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}/handlers/es

%files handlers-kinesis
%doc Readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}/handlers/kinesis

%changelog
%autochangelog
