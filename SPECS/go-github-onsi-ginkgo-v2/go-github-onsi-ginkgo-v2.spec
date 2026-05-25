# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ginkgo
%define go_import_path  github.com/onsi/ginkgo/v2
%define commit_id 4f62d7a74752034222d97d911f904d9be47ff7aa

Name:           go-github-onsi-ginkgo-v2
Version:        0+git20260518.4f62d7a
Release:        %autorelease
Summary:        Go library for github.com/onsi/ginkgo/v2
License:        MIT
URL:            https://github.com/onsi/ginkgo
#!RemoteAsset:  sha256:0091ba7240d1e23e5086233c13044180a11351105cfce4b2f49149da55547067
Source0:        https://github.com/onsi/ginkgo/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
Patch0:         2000-accept-quoted-semver-constraint-errors.patch
BuildArch:      noarch
BuildSystem:    golangmodules

# Integration tests run ginkgo watch and nested module commands. In OBS they
# timed out after 30s waiting for watched suites and failed module commands with
# "GOPROXY list is not the empty string, but contains no entries".
%define go_test_exclude %{go_import_path}/integration

BuildRequires:  go
BuildRequires:  go(github.com/gkampitakis/ciinfo)
BuildRequires:  go(github.com/gkampitakis/go-diff)
BuildRequires:  go(github.com/gkampitakis/go-snaps)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-task/slim-sprig/v3)
BuildRequires:  go(github.com/goccy/go-yaml)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/joshdk/go-junit)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/maruel/natural)
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/mfridman/tparse)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/match)
BuildRequires:  go(github.com/tidwall/pretty)
BuildRequires:  go(github.com/tidwall/sjson)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/onsi/ginkgo/v2) = %{version}

Requires:       go(github.com/gkampitakis/ciinfo)
Requires:       go(github.com/gkampitakis/go-diff)
Requires:       go(github.com/gkampitakis/go-snaps)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-task/slim-sprig/v3)
Requires:       go(github.com/goccy/go-yaml)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/pprof)
Requires:       go(github.com/joshdk/go-junit)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/kr/text)
Requires:       go(github.com/maruel/natural)
Requires:       go(github.com/Masterminds/semver/v3)
Requires:       go(github.com/mfridman/tparse)
Requires:       go(github.com/onsi/gomega)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(github.com/tidwall/gjson)
Requires:       go(github.com/tidwall/match)
Requires:       go(github.com/tidwall/pretty)
Requires:       go(github.com/tidwall/sjson)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/tools)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/check.v1)

%description
This package provides the Go library github.com/onsi/ginkgo/v2.

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
