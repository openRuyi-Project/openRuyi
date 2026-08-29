# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-vcr
%define go_import_path  github.com/dnaeon/go-vcr

# go-vcr is a test helper used by the Azure SDK resource-manager tests.
# Its own test suite ships a bundled vendor/ tree that is ignored in GOPATH
# mode; run the tests but tolerate failures from that layout mismatch.
%global go_test_ignore_failure 1

Name:           go-github-dnaeon-go-vcr
Version:        1.2.0
Release:        %autorelease
Summary:        Record and replay HTTP interactions for Go tests
License:        BSD-2-Clause
URL:            https://github.com/dnaeon/go-vcr
#!RemoteAsset:  sha256:91904d173052c3f72f3258cf4e165e0dbfd23a3b5cfc735169e39e59ab9a3c9a
Source0:        https://github.com/dnaeon/go-vcr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/dnaeon/go-vcr/cassette) = %{version}
Provides:       go(github.com/dnaeon/go-vcr/recorder) = %{version}

Requires:       go(gopkg.in/yaml.v2)

%description
go-vcr records outgoing HTTP interactions and replays them in tests,
allowing HTTP-based clients to be tested deterministically without a live
server. It is a test dependency of the Azure SDK resource-manager modules.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
