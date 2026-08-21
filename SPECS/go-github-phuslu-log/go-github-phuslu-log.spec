# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           log
%define go_import_path  github.com/phuslu/log

Name:           go-github-phuslu-log
Version:        1.0.127
Release:        %autorelease
Summary:        Structured logging library for Go
License:        MIT
URL:            https://github.com/phuslu/log
#!RemoteAsset:  sha256:061bfece7a424660b15b626635b5abcc3509e879c44e3f0d83fd8a0ba9eb1eca
Source0:        https://github.com/phuslu/log/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Keep the syslog test self-contained in restricted build environments.
# https://github.com/phuslu/log/pull/122
Patch0:         0001-use-local-udp-listener-for-syslog-tests.patch
# Select the matching output when stale rotated files are present.
Patch2000:      2000-select-the-matching-file-writer-output.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutlog)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/log)

Provides:       go(github.com/phuslu/log) = %{version}

Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/exporters/stdout/stdoutlog)
Requires:       go(go.opentelemetry.io/otel/sdk/log)

%description
Phuslu log provides high-performance structured logging, console and rotating
file writers, and standard-library logging integration.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
