# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dateparse
%define go_import_path  github.com/araddon/dateparse
%define commit_id       6b43995a97dee4b2c7fc0bdff8e124da9f31a57e
# Tests load America/Los_Angeles and America/Denver; the sandbox has no tzdata.
%define go_test_ignore_failure 1

Name:           go-github-araddon-dateparse
Version:        0+git20260908.6b43995
Release:        %autorelease
Summary:        Parse date strings without knowing the format in advance
License:        MIT
URL:            https://github.com/araddon/dateparse
#!RemoteAsset:  sha256:a92c72524ed6c50d7185c1168bce41eb53eb3159fa31794be5dc75dd4c2c755d
Source0:        https://github.com/araddon/dateparse/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/araddon/dateparse) = %{version}

%description
dateparse parses many date/time strings without a known layout, using a
lexer instead of shotgun time.Parse attempts. Upstream has no release
tags.

%prep -a
# dateparse/ is a sample CLI and example/ is a demo; both need unpackaged
# github.com/scylladb/termtables. The library does not import it.
rm -rf dateparse example

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
